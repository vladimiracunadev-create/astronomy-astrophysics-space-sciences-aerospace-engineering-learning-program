#!/usr/bin/env python3
"""B53-C26: publicacion de mapas. Convenciones ILUSTRATIVAS (no normas oficiales). Colores SINTETICOS en sRGB.
Contraste WCAG: formula de uso comun, no consultada. Tolerancia: contraste blanco/negro = 21 dentro de 1e-9."""
import itertools, json, platform

ESCALA, ANCHO_MM, PPP = 1_000_000, 0.5, 300
COLORES = {"A": "#1b9e77", "B": "#d95f02", "C": "#7570b3", "D": "#8aa63a", "E": "#a65628", "F": "#4daf4a"}
MIN = ["fuente", "marco_de_referencia", "proyeccion", "escala", "incertidumbre", "fecha", "licencia"]

def lum(hexa):
    c = [int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

def contraste(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def compute():
    mmu = ANCHO_MM * 1e-3 * ESCALA
    pix = 0.0254 / PPP * ESCALA
    cs = [contraste(COLORES[a], COLORES[b]) for a, b in itertools.combinations(sorted(COLORES), 2)]
    reg = {"fuente": "sintetica", "marco_de_referencia": "esfera ilustrativa", "proyeccion": "sinusoidal", "escala": "1:1000000"}
    faltan = [k for k in MIN if k not in reg or not reg[k]]
    return dict(mmu_m=mmu, mmu_km2=(2 * mmu / 1000) ** 2, pix_m=pix, c_min=min(cs), c_max=max(cs), npares=len(cs),
                nmal=sum(1 for c in cs if c < 1.5), campos_min=", ".join(MIN), faltan=", ".join(faltan), nfalt=len(faltan),
                bn=contraste("#ffffff", "#000000"))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"escala 1:{ESCALA}: unidad minima = {r['mmu_m']:.1f} m ; area minima = {r['mmu_km2']:.3f} km2 ; pixel a {PPP} ppp = {r['pix_m']:.2f} m")
    print(f"contraste blanco/negro = {r['bn']:.6f} ; leyenda: minimo {r['c_min']:.3f}, maximo {r['c_max']:.3f}, pares < 1.5: {r['nmal']} de {r['npares']}")
    print(f"metadatos: campos minimos = {r['campos_min']}")
    print(f"faltan en el registro de ejemplo ({r['nfalt']}): {r['faltan']}")
    print(json.dumps({"validacion": "incompleto" if r["nfalt"] else "completo"}))
    assert abs(r["bn"] - 21.0) < 1e-9 and r["nfalt"] == 3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
