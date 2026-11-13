# Datos y efemérides de los simuladores

Este documento explica **de dónde salen las posiciones**, **cómo se empaquetan**, **cómo se evalúan en el navegador** y **cuánto error tienen**. Cumple la regla del repositorio de declarar unidades, sistema de referencia, datos, versiones y tolerancias en toda simulación.

## Fuente oficial

| Qué | Fuente | Detalle |
|---|---|---|
| Planetas, Sol, Luna, Plutón (baricentro) | NASA/JPL **Horizons** (API v1.2), integración numérica **DE441** | Efemérides planetaria de largo plazo del JPL; en 2027–2050 coincide con DE440 a escala de metros. |
| Marte: Fobos y Deimos | Horizons, kernel `mar099` | Efemérides de satélites de Marte del JPL. |
| Júpiter | Horizons, kernels `jup365`, `jup347`, `jup348`, `jup349` (combinados con DE442) | Lunas galileanas y satélites menores e irregulares. |
| Saturno | Horizons, kernels `sat415`, `sat441`, `sat455`, `sat456`, `sat457`, `sat459`, `sat480` | Lunas mayores y satélites menores. |
| Urano | Horizons, kernel `ura184` | |
| Neptuno | Horizons, kernels `nep098`, `nep104` | |
| Ceres | Horizons, kernel `dawn_final` | Ajuste con datos de la misión Dawn. |

Los datos son **geométricos** (sin aberración de la luz ni deflexión relativista), no aparentes: corresponde a una vista «desde fuera» del sistema. El tiempo luz hasta un observador no se descuenta, porque no hay observador terrestre: la cámara es libre.

Las tablas se descargaron el **13 de noviembre de 2026** con [`herramientas/efemerides/generar_efemerides.py`](../../herramientas/efemerides/generar_efemerides.py). Horizons puede revisar sus ajustes más adelante (sobre todo las lunas pequeñas); regenerar los datos repite exactamente el procedimiento y la validación.

## Sistema de referencia, unidades y tiempo

- **Marco:** eclíptica y equinoccio medios J2000.0, alineado con el ICRF (`REF_PLANE=ECLIPTIC`, `REF_SYSTEM=ICRF`). El eje *z* apunta al polo norte eclíptico J2000.
- **Centro:** el Sol para los planetas (`500@10`) y el centro del planeta para sus lunas (`500@599`, etc.). La Luna está centrada en la Tierra (`500@399`).
- **Unidades:** kilómetros (posiciones) y días julianos (tiempo).
- **Escala de tiempo interna:** **TDB**. El simulador muestra y acepta **UTC**: `TDB = UTC + 69,184 s` (37 s de TAI−UTC + 32,184 s de TT−TAI + TDB−TT < 2 ms). Los segundos intercalares futuros son desconocidos —y la CGPM decidió eliminarlos hacia 2035—, así que el desfase se mantiene constante; el error posible hasta 2050 es de pocos segundos (≈ 0,002° en la Luna).
- **Soporte:** 2027-01-01 00:00 UTC a 2050-12-31 23:59:59 UTC. Fuera de ese rango el reloj se detiene.

## Formato de los archivos

Cada sistema son dos archivos en [`simuladores/datos/`](../datos/): `<sistema>.json` (metadatos) y `<sistema>.bin` (números).

- **`sol`**: Mercurio a Neptuno, el baricentro del sistema de Plutón y Ceres, heliocéntricos, `float64`.
- **`tierra`, `marte`, `jupiter`, `saturno`, `urano`, `neptuno`**: cada luna respecto del centro de su planeta.
- **`pluton`**: Plutón, Caronte, Estigia, Nix, Cerbero e Hidra respecto del **baricentro** del sistema (`500@9`), que queda fuera de Plutón (≈ 2 132 km de su centro).
- **`cielo.json`**: 5 044 estrellas hasta la magnitud 6, 493 nombres y las figuras de las 88 constelaciones (d3-celestial, BSD; Hipparcos/Tycho), ICRS J2000 sin movimiento propio.
- En el `.bin` cada cuerpo ocupa un bloque contiguo de posiciones `x, y, z` (km), *little-endian*, con **paso regular** `paso_min` (minutos) y época del primer nodo `t0` (JD TDB).
- Formatos: `f64` (planetas), `f32` (lunas mayores y de órbita lenta) o `i16` (lunas pequeñas y rápidas, escaladas por `escala_i16` km/unidad). La cuantización queda incluida en el error medido.
- Cada cuerpo declara `jd_valido_ini` y `jd_valido_fin`: **el intervalo donde la interpolación es válida**. Si Horizons no publica efemérides hasta 2050 (por ejemplo, Jano termina el 9 de enero de 2050), el cuerpo se **oculta** fuera de su cobertura; nunca se inventa una posición.

### Cómo se eligió el paso de cada tabla

Para cada luna se estima el periodo orbital con su estado inicial y el parámetro gravitatorio del planeta, y se elige el paso para tener un avance angular de **1 rad por nodo** (lunas pequeñas) o **0,6 rad** (radio ≥ 190 km y la Luna). Se corrige por excentricidad (velocidad angular en el periapsis) y se limita a 30 días. Los planetas usan 1, 2 o 4 días.

## Evaluación: interpolación de Lagrange de 10 puntos

El navegador (`motor/efemerides.js`) y Python (`herramientas/efemerides/lectura.py`) usan **exactamente la misma fórmula**: sobre nodos equiespaciados, polinomio de Lagrange con 4 nodos antes y 5 después del intervalo. Para una órbita circular con avance angular θ entre nodos, el error relativo es ≈ 870·θ¹⁰/10!; con θ = 1 rad es 2,4×10⁻⁴ del radio orbital y con θ = 0,6 rad es 2,3×10⁻⁷.

## Error medido, no supuesto

Por cada cuerpo, el generador pide a Horizons **120 épocas aleatorias que no son nodos** de la tabla (semilla fija) y compara. Esos valores quedan en [`datos/verificacion.json`](../datos/verificacion.json) y las pruebas de Node los reproducen sin red. El error máximo y el error cuadrático medio de cada cuerpo están en `datos/<sistema>.json` y en la [tabla de precisión](TABLA_DE_PRECISION.md).

Qué se observa: los planetas interiores quedan en **< 0,01 km**; los gigantes gaseosos en **≈ 10–170 km**, porque Horizons entrega el centro del *planeta*, que oscila alrededor del baricentro por la acción de sus lunas con periodos de pocos días (menores que el paso de 4 días) —es un efecto físico real, no un error de datos—; las lunas, del orden de **10⁻⁶–10⁻⁴ del radio orbital**. La validación automática exige un error máximo ≤ 6×10⁻⁴ del radio orbital para cada luna y ≤ 300 km para los planetas.

## Cuerpos sin datos

- **Dafne (Saturno XXXV, `635`)**: Horizons no tiene efemérides posteriores al 17 de enero de 2018. Se **excluye**.
- Los satélites con efemérides parciales (cobertura que termina antes de 2050) quedan ocultos tras su fecha final, como se indica arriba.

## Cómo regenerar

```bash
python -X utf8 herramientas/efemerides/generar_efemerides.py                 # todo (descarga cientos de MB a una caché local; tarda)
python -X utf8 herramientas/efemerides/generar_efemerides.py --solo sol,tierra
python herramientas/validar_simuladores.py                                    # valida datos, motor y páginas
```

La caché de respuestas (`herramientas/efemerides/_cache/`) no se versiona. Requiere `numpy`.
