# B40 — Universo temprano y radiación cósmica de fondo

> **Bloque de la estructura vigente.** Ver el [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md).

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial
**Área:** A03 — Astrofísica y ciencias fundamentales del universo
**Nivel:** N3 (fundamentos disciplinares) · **Clases:** 15 · **Carga:** por calibrar con el uso
**Estado:** guía pedagógica del bloque (resumen de qué se aprende en cada clase). Las clases enlazadas en la tabla ya están redactadas; todas conservan el estado E0 en el catálogo hasta registrar revisión disciplinar.

## 🎯 Propósito del bloque

Enseña **cómo se pasa del universo primordial a los mapas del fondo cósmico de microondas**: la inflación y su dinámica, el recalentamiento, el fondo de neutrinos, los problemas del horizonte y la planitud, las perturbaciones primordiales, los campos escalares, el espectro angular y la polarización, los efectos Sachs-Wolfe y Sunyaev-Zeldovich, los primeros planos galácticos, la pixelización de mapas, el ruido y el haz, los productos de datos y la varianza cósmica. Cada clase cierra con un cálculo verificable contra un caso analítico, dos vías independientes o una simulación con semilla fija, y distingue lo consultado de lo ilustrativo.

## 📚 Al terminar el bloque podrás

1. Integrar la dinámica de un campo escalar inflacionario y contar e-pliegues.
2. Estimar la temperatura de recalentamiento y la temperatura del fondo de neutrinos.
3. Calcular horizontes comóviles y explicar la planitud con números.
4. Relacionar el espectro primordial con n_s, r y la escala acústica.
5. Descomponer una polarización en modos E y B y medir la fuga por máscara.
6. Separar componentes de primer plano y reconocer la señal Sunyaev-Zeldovich.
7. Propagar ruido, haz y varianza cósmica a la incertidumbre de un espectro.

## 🧭 Secuencia del bloque

```mermaid
flowchart LR
    A["C01-C06<br/>Primordial"]
    B["C07-C11<br/>Señales"]
    C["C12-C15<br/>Datos"]
    A --> B --> C
```

**Descripción textual.** Tres tramos encadenados: universo primordial (C01–C06), anisotropías y señales (C07–C11) y mapas e instrumentos (C12–C15).

## 🗂️ Las 15 clases en resumen

**Navegación:** cada clase desarrollada enlaza a la anterior, a la siguiente y a este bloque; mientras una clase siga solo programada, su enlace lleva a su fila en esta tabla.

La columna «Evidencia» indica el producto que demostrará el aprendizaje. Los laboratorios usan datos **sintéticos** o **ilustrativos** (rotulados) o valores publicados con fuente y fecha.

### Tramo 1 · Universo primordial

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b40-c01"></a>[B40-C01](../clases/B40/B40-C01-inflacion-cosmica-motivacion-y-dinamica-basica/CLASE.md) | Inflación cósmica: motivación y dinámica básica | Inflación con ecuaciones de fondo y e-pliegues. | Ficha de la inflación cósmica |
| <a id="b40-c02"></a>[B40-C02](../clases/B40/B40-C02-recalentamiento-y-transicion-a-la-era-de-radiacion/CLASE.md) | Recalentamiento y transición a la era de radiación | Transferencia de energía del inflatón a radiación y temperatura de recalentamiento. | Ficha del recalentamiento |
| <a id="b40-c03"></a>[B40-C03](../clases/B40/B40-C03-desacoplamiento-de-neutrinos-y-fondo-cosmico-de-neutrinos/CLASE.md) | Desacoplamiento de neutrinos y fondo cósmico de neutrinos | Entropía, (4/11)^(1/3) y N_eff. | Ficha del fondo de neutrinos |
| <a id="b40-c04"></a>[B40-C04](../clases/B40/B40-C04-problemas-del-horizonte-y-de-la-planitud/CLASE.md) | Problemas del horizonte y de la planitud | Horizonte comóvil, ángulo causal y desvanecimiento de la curvatura. | Ficha de horizonte y planitud |
| <a id="b40-c05"></a>[B40-C05](../clases/B40/B40-C05-perturbaciones-primordiales-y-espectro-escalar/CLASE.md) | Perturbaciones primordiales y espectro escalar | Espectro de potencias, inclinación y razón tensor-escalar. | Ficha del espectro primordial |
| <a id="b40-c06"></a>[B40-C06](../clases/B40/B40-C06-campos-escalares-en-cosmologia-potenciales-y-evolucion/CLASE.md) | Campos escalares en cosmología: potenciales y evolución | Ecuación de Klein-Gordon y w promedio. | Ficha de campos escalares |

### Tramo 2 · Anisotropías y señales

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b40-c07"></a>[B40-C07](../clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md) | Espectro angular de potencias del CMB | Escala acústica, Cℓ y transformada de Legendre. | Ficha del espectro angular |
| <a id="b40-c08"></a>[B40-C08](../clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md) | Polarización E y B del fondo cósmico | Descomposición E/B en el plano y fuga por máscara. | Ficha de la polarización E/B |
| <a id="b40-c09"></a>[B40-C09](../clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md) | Efecto Sachs-Wolfe y efecto Sachs-Wolfe integrado | Meseta de Sachs-Wolfe y factor de crecimiento. | Ficha de Sachs-Wolfe |
| <a id="b40-c10"></a>[B40-C10](../clases/B40/B40-C10-emisiones-de-primer-plano-galacticas-y-su-separacion/CLASE.md) | Emisiones de primer plano galácticas y su separación | Leyes espectrales y combinación lineal interna. | Ficha de los primeros planos |
| <a id="b40-c11"></a>[B40-C11](../clases/B40/B40-C11-efecto-sunyaev-zeldovich-termico-y-cinematico/CLASE.md) | Efecto Sunyaev-Zeldovich térmico y cinemático | Función espectral, nulo en 217 GHz e y. | Ficha del efecto Sunyaev-Zeldovich |

### Tramo 3 · Mapas e instrumentos

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b40-c12"></a>[B40-C12](../clases/B40/B40-C12-analisis-de-mapas-del-cmb-pixelizacion-esferica-y-mascaras/CLASE.md) | Análisis de mapas del CMB: pixelización esférica y máscaras | Pixelización equiárea, ida y vuelta y fracción de cielo. | Ficha de pixelización y máscaras |
| <a id="b40-c13"></a>[B40-C13](../clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md) | Ruido, haz y covarianza instrumental en mapas del fondo | Ventana del haz, ruido blanco y covarianza. | Ficha del ruido y el haz |
| <a id="b40-c14"></a>[B40-C14](../clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md) | Productos de datos de Planck y misiones del CMB | Cabeceras FITS, conversión de unidades y verosimilitud. | Ficha de los productos de datos |
| <a id="b40-c15"></a>[B40-C15](../clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md) | Varianza cósmica y límites de las mediciones del fondo | Varianza cósmica 2/(2ℓ+1) y precisión de amplitud. | Ficha de la varianza cósmica |

## 🧵 Hilos que atraviesan el bloque

- **De la inflación al mapa:** C01–C06 fijan las condiciones iniciales; C07–C11 las convierten en señal observable; C12–C15 llevan la señal a mapas y límites de medición.
- **Dos vías independientes:** cada laboratorio contrasta con un caso analítico, una segunda forma de calcular o una simulación con semilla fija.
- **Incertidumbre:** C13 y C15 cuantifican el ruido y la varianza cósmica; C10 y C12 las contaminaciones y máscaras.
- **Observado frente a ilustrativo:** solo se citan con fecha los valores de Planck leídos en resúmenes de arXiv y las constantes de NIST; el resto de los números son ilustrativos o sintéticos y se rotulan.

## 📝 Evaluación del bloque (propuesta, por calibrar)

- Fichas y ejercicios por clase, con retroalimentación y recuperación con evidencia distinta.
- Portafolio: ficha del espectro angular (C07) y ficha de la varianza cósmica (C15).
- Las condiciones críticas (rotular lo sintético, no presentar un modelo de juguete como análisis de datos reales y citar solo lo consultado) no se compensan con promedio.

## ⚠️ Seguridad y límites

El bloque es educativo. Los modelos son simplificados y no sustituyen a los códigos de Boltzmann ni a los análisis publicados de las misiones; no se descargan ni procesan datos reales de Planck. Los valores publicados se citan con su fuente y fecha de consulta (solo resúmenes) y el resto de los números son ilustrativos y se rotulan como tales.

## Roles que lo usan

- [Cosmología y astrofísica extrema](../../rutas/cosmologia-y-astrofisica-extrema.md)

## Fuentes de orientación preliminar

- **[NIST-CODATA]** [NIST Fundamental Physical Constants (CODATA 2022)](https://physics.nist.gov/cuu/Constants/Table/allascii.txt) — Constantes físicas fundamentales.
- **[IAU-B3]** [UAI, Resolución B3 de 2015](https://arxiv.org/abs/1510.07674) — Valores nominales solares y planetarios.
- **[ADS]** [NASA Astrophysics Data System](https://ui.adsabs.harvard.edu/) — Índice bibliográfico de literatura astronómica y física.

> La asociación de estas fuentes es orientativa por bloque. Las fuentes realmente consultadas para cada afirmación se registran en la sección 11 de cada clase.

[🏠 Volver al programa](../../README.md) · [➡️ B41 — Óptica geométrica y diseño de telescopios](./B41-optica-geometrica-y-diseno-de-telescopios.md)
