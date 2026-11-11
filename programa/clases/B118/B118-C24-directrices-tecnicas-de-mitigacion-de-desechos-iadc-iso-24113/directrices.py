"""B118-C24 · Directrices técnicas de mitigación de desechos (IADC, ISO 24113).

Verificador de cumplimiento de misiones SINTÉTICAS frente a valores de IADC-02-01 Rev. 4 (enero de 2025; consultada el 2026-11-11 en el PDF
presentado a la UNOOSA como A/AC.105/C.1/2025/CRP.9): región LEO hasta 2000 km; región GEO +-200 km de 35786 km y +-15 grados de latitud;
vida residual en LEO <= 25 años; probabilidad de disposición exitosa >= 0,90 (objetivo 0,99); víctimas esperadas por reentrada <= 1e-4;
elevación del perigeo en GEO >= 235 km + 1000 CR A/m con e <= 0,003.
ISO 24113 NO se consultó (la página de ISO devolvió 403): sus requisitos no se codifican aquí.
Esto es una herramienta didáctica de lectura, no una verificación de conformidad ni asesoría legal o regulatoria.
Unidades: km, años, adimensional, m^2/kg. Radio ecuatorial 6378 km (valor de IADC). Tolerancia: comparaciones exactas en los bordes.
"""
import sys

RE_IADC = 6378.0
LEO_MAX = 2000.0
GEO_ALT, GEO_BANDA = 35786.0, 200.0


def region(perigeo, apogeo):
    # la región se evalúa sobre la órbita dada; las misiones que operaban en GEO llevan operaba_en="GEO" porque tras la disposición ya están fuera
    """Regiones protegidas cruzadas por el rango de altitudes (aproximación: se ignora la latitud para GEO)."""
    r = []
    if perigeo <= LEO_MAX:
        r.append("LEO")
    if apogeo >= GEO_ALT - GEO_BANDA and perigeo <= GEO_ALT + GEO_BANDA:
        r.append("GEO")
    return r


def verificar(m):
    fallas, notas = [], []
    reg = region(m["perigeo_km"], m["apogeo_km"])
    if "LEO" in reg:
        if m["vida_residual_anios"] > 25.0:
            fallas.append("vida residual > 25 anios")
        if m["p_disposicion"] < 0.90:
            fallas.append("probabilidad de disposicion < 0.90")
        elif m["p_disposicion"] < 0.99:
            notas.append("cumple 0.90 pero no el objetivo 0.99")
        if m.get("victimas_esperadas") is not None and m["victimas_esperadas"] > 1e-4:
            fallas.append("victimas esperadas > 1e-4")
    if "GEO" in reg or m.get("operaba_en") == "GEO":
        dh_min = 235.0 + 1000.0 * m["CR"] * m["A_m"]
        if m["elevacion_perigeo_km"] < dh_min:
            fallas.append(f"elevacion {m['elevacion_perigeo_km']:.1f} < {dh_min:.1f} km")
        if m["excentricidad_final"] > 0.003:
            fallas.append("excentricidad > 0.003")
    if not m.get("pasivada", False):
        fallas.append("sin pasivacion")
    if not reg:
        notas.append("fuera de las regiones protegidas")
    return reg, fallas, notas


MISIONES = [
    dict(id="M1", perigeo_km=540, apogeo_km=560, vida_residual_anios=4.0, p_disposicion=0.95, victimas_esperadas=5e-5, pasivada=True),
    dict(id="M2", perigeo_km=700, apogeo_km=720, vida_residual_anios=25.0, p_disposicion=0.90, victimas_esperadas=1e-4, pasivada=True),
    dict(id="M3", perigeo_km=700, apogeo_km=720, vida_residual_anios=25.01, p_disposicion=0.90, victimas_esperadas=1e-4, pasivada=True),
    dict(id="M4", perigeo_km=600, apogeo_km=620, vida_residual_anios=10.0, p_disposicion=0.89, victimas_esperadas=2e-5, pasivada=True),
    dict(id="M5", perigeo_km=800, apogeo_km=810, vida_residual_anios=20.0, p_disposicion=0.995, victimas_esperadas=2e-4, pasivada=True),
    dict(id="M6", operaba_en="GEO", perigeo_km=36034, apogeo_km=36040, CR=1.3, A_m=0.01, elevacion_perigeo_km=248.0, excentricidad_final=0.0003, pasivada=True),
    dict(id="M7", operaba_en="GEO", perigeo_km=36020, apogeo_km=36060, CR=1.3, A_m=0.01, elevacion_perigeo_km=247.9, excentricidad_final=0.0010, pasivada=True),
    dict(id="M8", operaba_en="GEO", perigeo_km=36100, apogeo_km=36900, CR=1.5, A_m=0.02, elevacion_perigeo_km=300.0, excentricidad_final=0.0031, pasivada=False),
    dict(id="M9", perigeo_km=30000, apogeo_km=31000, vida_residual_anios=0.0, p_disposicion=1.0, pasivada=True),
]
ESPERADO = {"M1": 0, "M2": 0, "M3": 1, "M4": 1, "M5": 1, "M6": 0, "M7": 1, "M8": 2, "M9": 0}


def compute():
    return [(m["id"], *verificar(m)) for m in MISIONES]


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Misiones SINTETICAS; valores de IADC-02-01 Rev.4 (consultada); ISO 24113 NO consultada; didactico, no es verificacion de conformidad.")
    res = compute()
    for mid, reg, fallas, notas in res:
        estado = "CUMPLE" if not fallas else "NO CUMPLE"
        print(f" {mid}: regiones {reg or ['ninguna']}; {estado}" + (": " + "; ".join(fallas) if fallas else "") + ("  [" + "; ".join(notas) + "]" if notas else ""))
        assert len(fallas) == ESPERADO[mid], (mid, fallas)
    print(f"Altura minima GEO para CR 1.3 y A/m 0.01: {235.0 + 1000 * 1.3 * 0.01:.1f} km")
    print("Pruebas superadas (9 misiones, incluidos los bordes 25.0/25.01 anios, 0.90/0.89, 1e-4/2e-4, 248.0/247.9 km).")


if __name__ == "__main__":
    main()
