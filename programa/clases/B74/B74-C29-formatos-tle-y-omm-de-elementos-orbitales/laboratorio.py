#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C29: formato TLE (dos lineas), suma de verificacion, lectura y conversion a un mensaje de elementos medios tipo OMM.

Todo SINTETICO: el objeto 'SINTETICO-99999' (numero de catalogo 99999 y designador 24999ZZZ, inventados) NO corresponde a ningun satelite real. Elementos: inclinacion 53.0000 deg, RAAN 120.5000 deg,
excentricidad 0.0012345, argumento del perigeo 85.0000 deg, anomalia media 275.0000 deg, movimiento medio 15.05000000 rev/dia, epoca 2026 dia 310.5 (todos ILUSTRATIVOS).
Columnas y regla de la suma de verificacion segun la pagina de CelesTrak consultada el 2026-11-10 (digitos suman su valor, el signo menos suma 1; letras, espacios, puntos y el signo mas suman 0; modulo 10;
columna 69). No se uso SGP4 ni se convierte entre elementos medios y osculadores. La relacion semieje-movimiento medio a = (mu/n^2)^(1/3) es de dos cuerpos (mu = 3.986004e14 m3/s2, ilustrativo, no consultado) y SOLO ilustra la
magnitud. Las claves del mensaje tipo OMM son ilustrativas y NO se contrastaron con el estandar CCSDS 502.0-B-3 (del que solo se consulto el alcance).
Pruebas: (1) longitudes de 69 caracteres; (2) la suma de verificacion coincide al releer; (3) todas las sustituciones de un digito son detectadas; se reporta la tasa de deteccion de transposiciones adyacentes de digitos distintos;
(4) ida y vuelta elementos -> TLE -> elementos con errores iguales o menores que la resolucion de cada campo.
Version: Python 3.12.9.
"""
import json, math, platform, sys

MU = 3.986004e14


def checksum(linea):
    s = 0
    for ch in linea[:68]:
        if ch.isdigit():
            s += int(ch)
        elif ch == "-":
            s += 1
    return s % 10


def construye(el):
    l1 = ("1 {sat:05d}U {des:<8s} {ep:014.8f} {nd:>10s} {ndd:>8s} {bs:>8s} 0 {nel:4d}").format(
        sat=el["sat"], des=el["des"], ep=el["epoca"], nd=" .00000000", ndd=" 00000-0", bs=" 00000-0", nel=el["nel"])
    l1 = l1.replace("U 24999ZZZ", "U 24999ZZZ")
    l1 = l1[:68].ljust(68)
    l2 = "2 {sat:05d} {i:8.4f} {raan:8.4f} {e:07d} {w:8.4f} {M:8.4f} {n:11.8f}{rev:5d}".format(
        sat=el["sat"], i=el["i"], raan=el["raan"], e=int(round(el["e"] * 1e7)), w=el["w"], M=el["M"], n=el["n"], rev=el["rev"])
    l2 = l2.ljust(68)
    return l1 + str(checksum(l1)), l2 + str(checksum(l2))


def lee(l1, l2):
    return {
        "sat": int(l1[2:7]), "clase": l1[7], "des": l1[9:17].strip(), "anio2": int(l1[18:20]), "dia": float(l1[20:32]),
        "i": float(l2[8:16]), "raan": float(l2[17:25]), "e": float("0." + l2[26:33].strip()), "w": float(l2[34:42]),
        "M": float(l2[43:51]), "n": float(l2[52:63]), "rev": int(l2[63:68]),
        "ck1": int(l1[68]), "ck2": int(l2[68]),
    }


def main():
    el = dict(sat=99999, des="24999ZZZ", epoca=26310.5, nel=999, i=53.0, raan=120.5, e=0.0012345, w=85.0, M=275.0, n=15.05, rev=12345)
    l1, l2 = construye(el)
    out = [f"Python {platform.python_version()} (objeto SINTETICO; numero de catalogo 99999 inventado)"]
    out.append(l1)
    out.append(l2)
    res = {}
    ok = len(l1) == 69 and len(l2) == 69
    p = lee(l1, l2)
    ok &= checksum(l1) == p["ck1"] and checksum(l2) == p["ck2"]
    out.append(f"Longitudes: {len(l1)} y {len(l2)} ; sumas de verificacion: {p['ck1']} y {p['ck2']} (recalculadas: {checksum(l1)} y {checksum(l2)})")
    res.update(ck1=p["ck1"], ck2=p["ck2"], len1=len(l1), len2=len(l2))
    # sustituciones de digitos
    total = det = 0
    for L in (l1, l2):
        for k in range(68):
            if L[k].isdigit():
                for d in "0123456789":
                    if d != L[k]:
                        total += 1
                        M = L[:k] + d + L[k + 1:68] + L[68]
                        if checksum(M) != int(L[68]):
                            det += 1
    # transposiciones adyacentes
    tt = dt = 0
    for L in (l1, l2):
        for k in range(67):
            if L[k].isdigit() and L[k + 1].isdigit() and L[k] != L[k + 1]:
                tt += 1
                M = L[:k] + L[k + 1] + L[k] + L[k + 2:]
                if checksum(M) != int(L[68]):
                    dt += 1
    out.append(f"Sustituciones de un digito: {det} de {total} detectadas ({100*det/total:.1f} %)")
    out.append(f"Transposiciones adyacentes de digitos distintos: {dt} de {tt} detectadas ({100*dt/tt:.1f} %)")
    res.update(sust_tot=total, sust_det=det, trans_tot=tt, trans_det=dt)
    ok &= det == total
    # elementos leidos
    out.append(f"Leido: i = {p['i']} deg ; RAAN = {p['raan']} deg ; e = {p['e']:.7f} ; w = {p['w']} deg ; M = {p['M']} deg ; n = {p['n']} rev/dia ; epoca = 20{p['anio2']} dia {p['dia']}")
    # resolucion
    n_rad = p["n"] * 2 * math.pi / 86400
    a = (MU / n_rad**2) ** (1 / 3)
    per = 86400 / p["n"]
    out.append(f"Magnitud de dos cuerpos: periodo = {per/60:.4f} min ; semieje a = {a/1e3:.3f} km (solo ilustrativo; los elementos del TLE son medios para SGP4)")
    res.update(per_min=per / 60, a_km=a / 1e3)
    dM = 5e-5  # grados, medio ultimo digito
    desp = a * math.radians(dM)
    out.append(f"Resolucion de la anomalia media (0.0001 deg): medio paso = {dM} deg -> {desp:.2f} m a lo largo de la orbita")
    dn = 5e-9 * 86400 / (24 * 3600)  # no usado
    ddn = 0.5e-8  # rev/dia
    da = a * (2 / 3) * ddn / p["n"]
    out.append(f"Resolucion del movimiento medio (1e-8 rev/dia): medio paso = {ddn:.1e} rev/dia -> {da*1e3:.3f} mm en el semieje")
    res.update(desp_m=desp, da_mm=da * 1e3)
    # ida y vuelta
    ok &= abs(p["i"] - el["i"]) <= 5e-5 and abs(p["e"] - el["e"]) <= 5e-8 and abs(p["n"] - el["n"]) <= 5e-9
    # mensaje tipo OMM (claves ilustrativas)
    omm = {
        "OBJECT_NAME": "SINTETICO-99999", "OBJECT_ID": p["des"], "CENTER_NAME": "EARTH", "REF_FRAME": "TEME (por convencion de TLE; no verificado contra CCSDS)",
        "MEAN_ELEMENT_THEORY": "SGP4 (nombre convencional; no se ejecuta)", "EPOCH": f"20{p['anio2']}-DOY {p['dia']}",
        "MEAN_MOTION": p["n"], "ECCENTRICITY": p["e"], "INCLINATION": p["i"], "RA_OF_ASC_NODE": p["raan"], "ARG_OF_PERICENTER": p["w"], "MEAN_ANOMALY": p["M"],
        "NORAD_CAT_ID": p["sat"], "REV_AT_EPOCH": p["rev"],
    }
    txt = json.dumps(omm, indent=1)
    out.append(f"Mensaje tipo OMM (JSON, claves ILUSTRATIVAS): {len(omm)} campos, {len(txt)} bytes")
    res.update(omm_n=len(omm), omm_b=len(txt))
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
