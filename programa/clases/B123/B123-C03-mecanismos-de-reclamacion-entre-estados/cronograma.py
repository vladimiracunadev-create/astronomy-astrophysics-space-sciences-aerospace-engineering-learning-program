"""B123-C03 - Cronograma SINTETICO de una reclamacion entre Estados.

Fechas SINTETICAS (ningun caso real). Solo biblioteca estandar. Fechas calendario ISO 8601.
Normativa (leida en resumen, ver CLASE.md): Convenio de 1972, arts. IX, X, XI, XIV, XV, XIX.
Los plazos se aproximan sumando anos calendario; un caso real exige el texto oficial y un profesional.
"""
import sys
from datetime import date


def mas_un_ano(d):
    try:
        return d.replace(year=d.year + 1)
    except ValueError:  # 29 de febrero
        return d.replace(year=d.year + 1, day=28)


def cronograma(dano, presentacion, comision_solicitada):
    """Devuelve las etapas con su fecha limite o estado."""
    lim_presentacion = mas_un_ano(dano)
    lim_negociacion = mas_un_ano(presentacion)
    etapas = []
    etapas.append(("Dano", dano, ""))
    etapas.append(("Limite para presentar (art. X)", lim_presentacion, "OK" if presentacion <= lim_presentacion else "FUERA DE PLAZO"))
    etapas.append(("Presentacion por via diplomatica (art. IX)", presentacion, ""))
    etapas.append(("Fin del ano de negociacion (art. XIV)", lim_negociacion, ""))
    ok_comision = comision_solicitada >= lim_negociacion
    etapas.append(("Solicitud de comision", comision_solicitada, "OK" if ok_comision else "ANTICIPADA (sin agotar la negociacion)"))
    return etapas


def decision_limite(constitucion):
    """La comision decide en un ano desde su constitucion, salvo prorroga (art. XIX, segun el resumen consultado)."""
    return mas_un_ano(constitucion)


def composicion(parte_a_nombra, parte_b_nombra, acuerdan_presidente):
    """art. XV: tres miembros; si no hay acuerdo sobre el presidente, puede nombrarlo el Secretario General de la ONU."""
    miembros = 0
    miembros += 1 if parte_a_nombra else 0
    miembros += 1 if parte_b_nombra else 0
    if acuerdan_presidente:
        miembros += 1
        quien = "presidente por acuerdo"
    else:
        quien = "presidente por el Secretario General (a solicitud, tras el plazo)"
    return miembros, quien


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Fechas SINTETICAS")
    for dano, pres, com in [(date(2026, 3, 1), date(2026, 11, 20), date(2027, 11, 20)),
                            (date(2026, 3, 1), date(2027, 4, 2), date(2027, 6, 1))]:
        print(f"Caso dano {dano}, presentacion {pres}, comision {com}:")
        for nombre, f, est in cronograma(dano, pres, com):
            print(f"  {f}  {nombre} {est}")
    c = date(2028, 1, 10)
    print(f"Comision constituida {c}: decision en un ano -> {decision_limite(c)}")
    for a, b, p in [(True, True, True), (True, True, False)]:
        n, q = composicion(a, b, p)
        print(f"Composicion: miembros nombrados = {n}; {q}")
    assert mas_un_ano(date(2024, 2, 29)) == date(2025, 2, 28)
    assert cronograma(date(2026, 3, 1), date(2027, 4, 2), date(2027, 6, 1))[1][2] == "FUERA DE PLAZO"
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
