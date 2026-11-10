"""B59-C13 · Impresión por capas de una cúpula: volumen, tiempo, convergencia y voladizo.

Datos ILUSTRATIVOS (no consultados): cúpula hemisférica de radio exterior 3,0 m y espesor de pared 0,30 m;
cordón de ancho w = 0,05 m y altura de capa h variable; velocidad de impresión v = 0,10 m/s.
Modelo: capa k a la altura z_k = (k + 1/2) h aporta un anillo de volumen pi (r_o^2 - r_i^2) h con
r_o = sqrt(Ro^2 - z^2), r_i = sqrt(Ri^2 - z^2) (solo mientras z < Ri; después el casquete es macizo en el cenit
y se trata como disco). Volumen analítico del casquete: (2 pi/3)(Ro^3 - Ri^3).
Tiempo de impresión = suma de (longitud de trayectoria) / v con longitud = anillos de ancho w.
Restricción de voladizo: el desplazamiento radial entre capas |dr| = h z/r no debe exceder w/2.
Unidades SI. Sin refuerzo, sin curado, sin pandeo de la pared fresca.
Tolerancias: volumen por capas frente a analítico < 0,2 % con h = 0,02 m; error decreciente y < 0,1 % para h <= 0,04 m.
"""
import math
import platform

RO, T_PARED = 3.0, 0.30
RI = RO - T_PARED
W, V_IMP = 0.05, 0.10


def volumen_capas(h):
    n = int(RO / h)
    vol = 0.0
    path = 0.0
    for k in range(n):
        z = (k + 0.5) * h
        ro = math.sqrt(RO ** 2 - z ** 2)
        if z < RI:
            ri = math.sqrt(RI ** 2 - z ** 2)
            vol += math.pi * (ro ** 2 - ri ** 2) * h
            # longitud de trayectoria: anillos concentricos de ancho W entre ri y ro (radio medio)
            ancho = ro - ri
        else:
            vol += math.pi * ro ** 2 * h
            ancho = ro
        n_anillos = max(1, round(ancho / W))
        for j in range(n_anillos):
            r = (ro - (j + 0.5) * ancho / n_anillos)
            path += 2 * math.pi * r
    return vol, path


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    v_an = 2 * math.pi / 3 * (RO ** 3 - RI ** 3)
    print(f"Volumen analitico del casquete = {v_an:.4f} m^3 (Ro = {RO} m, Ri = {RI:.2f} m)")
    errs = []
    print("h [m]   capas   volumen por capas [m^3]   error relativo   longitud de trayectoria [km]   tiempo [h]")
    for h in (0.08, 0.04, 0.02, 0.01):
        v, p = volumen_capas(h)
        e = abs(v - v_an) / v_an
        errs.append(e)
        print(f"{h:5.2f}  {int(RO/h):5d}  {v:23.4f}  {e:14.2e}  {p/1000:27.3f}  {p/V_IMP/3600:10.2f}")
    assert errs[2] < 2e-3, "volumen con h=0,02 fuera de tolerancia"
    orden = math.log(errs[0] / errs[1]) / math.log(2)
    print(f"Orden de convergencia entre h = 0,08 y 0,04 = {orden:.2f} (esperado ~2); despues el error cae de forma irregular porque la capa que cruza el radio interior cambia de forma")
    assert errs[1] > errs[2] > errs[3] and all(e < 1e-3 for e in errs[1:])
    # Voladizo: z/r <= w/(2h) => tan(phi) <= 0,5 w/h
    h = 0.02
    tmax = 0.5 * W / h
    phi = math.atan(tmax)
    z_lim = RO * math.sin(phi)
    print(f"Voladizo maximo por capa w/2 = {W/2*1000:.0f} mm ; tan(phi) maximo = {tmax:.2f} -> phi = {math.degrees(phi):.1f} grados desde la base; altura limite = {z_lim:.2f} m de {RO} m")
    # Volumen por encima del limite
    v_tot, _ = volumen_capas(0.01)
    # fraccion del volumen por encima de z_lim (analitica por integral de casquete)
    def vol_hasta(z):
        zr = min(z, RI)
        return math.pi * (RO ** 2 * z - z ** 3 / 3) - (math.pi * (RI ** 2 * zr - zr ** 3 / 3))
    frac = 1 - vol_hasta(z_lim) / v_an
    print(f"Fraccion del volumen que queda por encima de la altura limite = {100*frac:.1f} %")
    # Tiempo por analitica: V / (w h v)
    v, p = volumen_capas(0.02)
    t_vol = v_an / (W * 0.02 * V_IMP) / 3600
    print(f"Tiempo = {p/V_IMP/3600:.2f} h por trayectoria ; V/(w h v) = {t_vol:.2f} h ; diferencia relativa {abs(p/V_IMP/3600-t_vol)/t_vol:.2%}")
    assert abs(p / V_IMP / 3600 - t_vol) / t_vol < 0.15
    # Masa con densidad aparente 1500 kg/m3 (ILUSTRATIVA)
    print(f"Masa de la cupula con 1 500 kg/m^3 = {v_an*1500/1000:.1f} t")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
