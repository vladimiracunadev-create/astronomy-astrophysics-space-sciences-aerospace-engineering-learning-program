"""B67-C04: recurso, categoria por confianza y reserva con factores modificadores (SINTETICO).

Masa de hielo en un bloque:  M = A * h * rho * w
  A  area [m2] ; h espesor del deposito [m] ; rho densidad aparente [kg m-3] ;
  w  fraccion masica de hielo [adimensional, 0-1].
Todos los valores son inventados para la clase. La regla de categorias (umbrales de
incertidumbre relativa) es DIDACTICA: no reproduce ninguna norma de reporte minero.
Requiere solo numpy.
"""
import sys
import numpy as np

A, SA = 4.0e6, 0.02 * 4.0e6          # area 4 km2, incertidumbre 2 %
H, SH = 2.0, 0.15 * 2.0              # espesor 2 m, 15 %
RHO, SRHO = 1500.0, 0.05 * 1500.0    # densidad aparente, 5 %
W_MEDIA, W_FORMA = 0.03, 4.0         # w ~ Gamma(forma=4, media=0.03) por muestra
Z90 = 1.6449                         # cuantil normal bilateral 90 %
F_ACC, F_REC = 0.6, 0.8              # factores modificadores ilustrativos


def categoria(rel90):
    """semiancho relativo del intervalo al 90 % -> categoria didactica."""
    if rel90 <= 0.15:
        return "Medido"
    if rel90 <= 0.35:
        return "Indicado"
    return "Inferido"


def intervalo_w(muestras):
    m = muestras.mean()
    s = muestras.std(ddof=1)
    return m, Z90 * s / np.sqrt(len(muestras))


def main():
    print(f"Python {sys.version.split()[0]} ; numpy {np.__version__}")
    print("DATOS SINTETICOS: bloque, densidades y regla de categorias inventados")
    rng = np.random.default_rng(6704)
    escala = W_MEDIA / W_FORMA
    print("n muestras  w medio [%]  semiancho w [%]  M [kt]  semiancho M [%] (analitico / MC)  categoria")
    res = {}
    for n in (3, 12, 48):
        w = rng.gamma(W_FORMA, escala, size=n)
        wm, dw = intervalo_w(w)
        M = A * H * RHO * wm / 1e6  # kt
        rel_w = dw / wm
        rel = np.sqrt((SA / A) ** 2 + (SH / H) ** 2 + (SRHO / RHO) ** 2 + (dw / wm) ** 2)
        # Monte Carlo: todas las entradas como normales con su sigma (w con sigma = dw/Z90)
        N = 200000
        sim = (rng.normal(A, SA, N) * rng.normal(H, SH, N) * rng.normal(RHO, SRHO, N)
               * rng.normal(wm, dw / Z90, N)) / 1e9
        q5, q95 = np.percentile(sim, [5, 95])
        rel_mc = (q95 - q5) / 2 / sim.mean()
        # el semiancho 90 % de un producto de normales con sigmas relativas pequenas:
        # sigma_rel_total * Z90 ; el 'rel' analitico ya usa dw (=Z90 sigma_w) para w:
        sig_tot = np.sqrt((SA / A) ** 2 + (SH / H) ** 2 + (SRHO / RHO) ** 2 + (dw / Z90 / wm) ** 2)
        rel_an = Z90 * sig_tot
        cat = categoria(rel_an)
        res[n] = (M, rel_an, cat)
        print(f"  {n:3d}      {100 * wm:6.2f}       {100 * dw:6.2f}        {M:7.2f}   {100 * rel_an:6.1f} / {100 * rel_mc:6.1f}        {cat}")
        assert abs(rel_an - rel_mc) < 0.03, "analitico y Monte Carlo difieren"
    # reservas: solo Medido e Indicado se convierten
    print("Conversion a reservas (factores modificadores F_acc=0,6; F_rec=0,8; solo Medido/Indicado):")
    total_rec = total_res = 0.0
    for n, (M, rel, cat) in res.items():
        r = M * F_ACC * F_REC if cat in ("Medido", "Indicado") else 0.0
        total_rec += M
        total_res += r
        print(f"  bloque con n={n:2d}: recurso {M:7.2f} kt ; reserva {r:7.2f} kt ({cat})")
    print(f"Total recursos {total_rec:.2f} kt ; total reservas {total_res:.2f} kt")
    assert total_res <= total_rec * F_ACC * F_REC + 1e-9
    # cobertura del intervalo de w con z (comprobacion de la regla)
    print("Cobertura empirica del intervalo al 90 % de w (5000 repeticiones, semilla 6704):")
    cob = {}
    for n in (3, 12, 48):
        ok = 0
        for _ in range(5000):
            w = rng.gamma(W_FORMA, escala, size=n)
            m, d = intervalo_w(w)
            ok += (m - d <= W_MEDIA <= m + d)
        cob[n] = ok / 5000
        print(f"  n={n:2d}: {100 * cob[n]:.1f} %")
    assert 0.87 <= cob[48] <= 0.93
    assert cob[3] < cob[48]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
