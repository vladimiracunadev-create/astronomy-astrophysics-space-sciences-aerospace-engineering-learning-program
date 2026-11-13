# Tabla de precisión de las efemérides

Generada automáticamente por `herramientas/efemerides/tabla_precision.py` a partir de `simuladores/datos/*.json`; no se edita a mano.

El **error** es la distancia entre la posición interpolada y la que entrega JPL Horizons en 120 épocas aleatorias que no son nodos de la tabla (máximo y valor cuadrático medio, en km). «Nodos/órbita» es el número aproximado de nodos por revolución. «Cobertura» sólo aparece cuando Horizons no publica efemérides hasta el 31-12-2050 (el cuerpo se oculta después). Método: [Datos y efemérides](DATOS_Y_EFEMERIDES.md).

## Sistema Solar (heliocéntrico)

10 cuerpos · peor error máximo: Júpiter (165,04 km). Marco: Eclíptica y equinoccio J2000 (ICRF), geométrico; centro `500@10`.

| ID | Cuerpo | Radio (km) | Paso | Nodos/órbita | Formato | Err. máx. (km) | Err. rms (km) | Cobertura |
|---:|---|---:|---:|---:|---|---:|---:|---|
| 199 | Mercurio | 2 439,4 | 1 d | 88.0 | f64 | 0,002 | 0,001 |  |
| 299 | Venus | 6 051,8 | 2 d | 112.4 | f64 | 0,000 | 0,000 |  |
| 399 | Tierra | 6 378,1 | 1 d | 365.3 | f64 | 0,000 | 0,000 |  |
| 499 | Marte | 3 396,2 | 2 d | 343.5 | f64 | 0,000 | 0,000 |  |
| 599 | Júpiter | 71 492,0 | 4 d | 1083.1 | f64 | 165,041 | 93,503 |  |
| 699 | Saturno | 60 268,0 | 4 d | 2689.8 | f64 | 10,795 | 4,742 |  |
| 799 | Urano | 25 559,0 | 4 d | 7672.1 | f64 | 20,441 | 10,177 |  |
| 899 | Neptuno | 24 764,0 | 4 d | 15045.5 | f64 | 142,917 | 102,895 |  |
| 9 | Plutón (baricentro del sistema) | 1 188,3 | 4 d | 22640.0 | f64 | 0,000 | 0,000 |  |
| 2000001 | Ceres | 469,7 | 2 d | 840.0 | f64 | 0,000 | 0,000 |  |

## Tierra: la Luna

1 cuerpos · peor error máximo: Moon (0,02 km). Marco: Eclíptica y equinoccio J2000 (ICRF), geométrico; centro `500@399`.

| ID | Cuerpo | Radio (km) | Paso | Nodos/órbita | Formato | Err. máx. (km) | Err. rms (km) | Cobertura |
|---:|---|---:|---:|---:|---|---:|---:|---|
| 301 | Moon | 1 737,4 | 751 min | 52.7 | f32 | 0,019 | 0,010 |  |

## Marte

2 cuerpos · peor error máximo: Phobos (2,35 km). Marco: Eclíptica y equinoccio J2000 (ICRF), geométrico; centro `500@499`.

| ID | Cuerpo | Radio (km) | Paso | Nodos/órbita | Formato | Err. máx. (km) | Err. rms (km) | Cobertura |
|---:|---|---:|---:|---:|---|---:|---:|---|
| 401 | Phobos | 11,1 | 63 min | 7.3 | i16 | 2,350 | 1,195 |  |
| 402 | Deimos | 6,2 | 260 min | 7.0 | i16 | 1,919 | 1,160 |  |
