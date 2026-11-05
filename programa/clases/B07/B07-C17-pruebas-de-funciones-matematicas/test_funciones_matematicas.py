# SPDX-License-Identifier: Apache-2.0
"""Pruebas pytest de funciones_matematicas.py (B07-C17).

Cada prueba compara con un caso analítico o con una propiedad matemática, no con el
resultado que da la propia función. Tolerancias: pytest.approx con rel=1e-12 salvo aviso.
Requiere pytest 9.2.0 (Python 3.12.9).
"""

import math

import pytest

import funciones_matematicas as fm


def test_volumen_esfera_unitaria():
    assert fm.volumen_esfera(1.0) == pytest.approx(4.0 * math.pi / 3.0, rel=1e-12)


def test_volumen_cero():
    assert fm.volumen_esfera(0.0) == 0.0                      # caso borde


@pytest.mark.parametrize("radio", [0.5, 1.0, 6371.0, 1e-3])
def test_volumen_escala_con_el_cubo(radio):
    # propiedad: duplicar el radio multiplica el volumen por 8
    assert fm.volumen_esfera(2 * radio) == pytest.approx(8 * fm.volumen_esfera(radio), rel=1e-12)


def test_volumen_negativo_lanza_error():
    with pytest.raises(ValueError, match="radio negativo"):
        fm.volumen_esfera(-1.0)


@pytest.mark.parametrize("a, b, c, esperadas", [
    (1, -3, 2, (1.0, 2.0)),            # (x-1)(x-2)
    (1, 0, -4, (-2.0, 2.0)),           # x² = 4
    (2, -10, 12, (2.0, 3.0)),
    (1, -2, 1, (1.0, 1.0)),            # raíz doble
])
def test_raices_conocidas(a, b, c, esperadas):
    assert fm.raices_estables(a, b, c) == pytest.approx(esperadas, rel=1e-12)


def test_raices_cumplen_vieta():
    r1, r2 = fm.raices_estables(1.0, -1e8, 1.0)
    assert r1 * r2 == pytest.approx(1.0, rel=1e-12)           # producto = c/a
    assert r1 + r2 == pytest.approx(1e8, rel=1e-12)           # suma = -b/a


def test_raiz_pequena_estable_vs_ingenua():
    esperada = 1e-8                                           # raíz pequeña de x² − 1e8 x + 1 (a 1e-16 relativo)
    estable, _ = fm.raices_estables(1.0, -1e8, 1.0)
    ingenua, _ = fm.raices_ingenuas(1.0, -1e8, 1.0)
    assert estable == pytest.approx(esperada, rel=1e-12)
    assert ingenua != pytest.approx(esperada, rel=1e-2)       # la ingenua falla por más de 1 %


def test_discriminante_negativo_y_a_cero():
    with pytest.raises(ValueError, match="discriminante negativo"):
        fm.raices_estables(1, 0, 1)
    with pytest.raises(ValueError, match="a no puede ser 0"):
        fm.raices_estables(0, 1, 1)


def test_periodo_kepler_de_la_tierra_y_de_marte():
    assert fm.periodo_kepler_anios(1.0) == 1.0
    a_marte = 227.956 / 149.598                                # distancia relativa (datos publicados)
    assert fm.periodo_kepler_anios(a_marte) == pytest.approx(686.980 / 365.256, rel=1e-3)   # 0,1 %


@pytest.mark.parametrize("malo", [0.0, -1.0, float("nan")])
def test_periodo_rechaza_entradas_invalidas(malo):
    with pytest.raises(ValueError):
        fm.periodo_kepler_anios(malo)
