# B64 — Extremófilos y límites de la vida

> **Bloque de la estructura vigente.** Ver el [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md).

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial
**Área:** A05 — Ciencias planetarias, astroquímica y habitabilidad
**Nivel:** N3 (fundamentos disciplinares) · **Clases:** 7 · **Carga:** por calibrar con el uso
**Estado:** guía pedagógica del bloque (resumen de qué se aprende en cada clase). Las clases enlazadas en la tabla ya están redactadas; todas conservan el estado E0 en el catálogo hasta registrar revisión disciplinar.

## 🎯 Propósito del bloque

Enseña **dónde se detienen los límites de la vida que conocemos y cómo se cuantifican esos límites**: la tolerancia a la radiación ionizante y la reparación del ADN, el calor de los termófilos e hipertermófilos, el frío y la lentitud metabólica de los psicrófilos, la sal y la actividad del agua de los halófilos, el pH de los acidófilos y alcalófilos, la protección colectiva de los biofilms y, por último, el cultivo prudente de organismos no patógenos en cámaras que imitan algunas condiciones de otros mundos. Cada clase cierra con un laboratorio en Python que contrasta un modelo simple con un caso analítico, con dos vías independientes o con una simulación de semilla fija, y distingue lo consultado de lo ilustrativo.

## 📚 Al terminar el bloque podrás

1. Calcular la probabilidad de supervivencia a una dosis de radiación con un modelo de roturas de doble cadena y explicar qué significa la capacidad de reparación.
2. Ajustar una curva de crecimiento frente a la temperatura y estimar la presión que mantiene agua líquida sobre 100 °C.
3. Escalar tasas metabólicas con la ecuación de Arrhenius hacia temperaturas bajo cero y leer el resultado como un orden de magnitud, no como una predicción.
4. Relacionar la actividad del agua con la molalidad de una salmuera y con la presión osmótica que soporta una célula.
5. Calcular la fuerza protonmotriz y el atrapamiento de un ácido débil en acidófilos y alcalófilos.
6. Resolver la difusión con reacción en un biofilm y decidir cuándo el interior queda en carencia.
7. Planificar, con criterios de bioseguridad, un cultivo no patógeno en una cámara análoga y declarar qué parte del ambiente real no reproduce.

## 🧭 Secuencia del bloque

```mermaid
flowchart LR
    A["C01-C05<br/>Límites fisicoquímicos"]
    B["C06-C07<br/>Comunidades y laboratorio"]
    A --> B
```

**Descripción textual.** Dos tramos encadenados: los límites que imponen la radiación, la temperatura, el agua y el pH a una célula (C01–C05), y cómo viven en comunidad y cómo se cultivan con seguridad (C06–C07).

## 🗂️ Las 7 clases en resumen

**Navegación:** cada clase desarrollada enlaza a la anterior, a la siguiente y a este bloque; mientras una clase siga solo programada, su enlace lleva a su fila en esta tabla.

La columna «Evidencia» indica el producto que demostrará el aprendizaje. Los laboratorios usan datos **sintéticos** o **ilustrativos** (rotulados) o valores publicados con fuente y fecha.

### Tramo 1 · Límites fisicoquímicos

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b64-c01"></a>[B64-C01](../clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md) | Radiotolerancia biológica y reparación del ADN | Roturas de doble cadena como proceso de Poisson, capacidad de reparación y dosis D10. | Ficha de la radiotolerancia |
| <a id="b64-c02"></a>[B64-C02](../clases/B64/B64-C02-termofilos-e-hipertermofilos/CLASE.md) | Termófilos e hipertermófilos | Temperaturas cardinales, energía de activación aparente y presión de vapor del agua. | Ficha de la curva térmica |
| <a id="b64-c03"></a>[B64-C03](../clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md) | Psicrófilos y vida en frío | Escalado de Arrhenius, Q10 creciente y tiempos de renovación a temperaturas bajo cero. | Ficha del escalado en frío |
| <a id="b64-c04"></a>[B64-C04](../clases/B64/B64-C04-halofilos-y-vida-en-salmueras/CLASE.md) | Halófilos y vida en salmueras | Actividad del agua, presión osmótica y estrategias de equilibrio osmótico. | Ficha de la salmuera |
| <a id="b64-c05"></a>[B64-C05](../clases/B64/B64-C05-acidofilos-y-alcalofilos/CLASE.md) | Acidófilos y alcalófilos | Fuerza protonmotriz, potencial de membrana invertido y atrapamiento de ácidos débiles. | Ficha del gradiente de pH |

### Tramo 2 · Comunidades y laboratorio

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b64-c06"></a>[B64-C06](../clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md) | Biofilms en ambientes extremos | Matriz de EPS, módulo de Thiele y factor de efectividad de una película. | Ficha del biofilm |
| <a id="b64-c07"></a>[B64-C07](../clases/B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md) | Cultivo de extremófilos no patógenos en condiciones análogas | Balance de gases de una cámara, crecimiento logístico y límites de un análogo. | Ficha del cultivo en cámara análoga |

## 🧵 Hilos que atraviesan el bloque

- **Un límite, una magnitud:** cada clase reduce un límite de la vida a una magnitud medible (dosis, temperatura, actividad del agua, ΔpH, módulo de Thiele) y a una ecuación que la conecta con el resultado.
- **Arrhenius como lengua común:** C02 y C03 comparten la misma forma funcional; C05 y C07 reutilizan R, F y la ley del gas ideal con constantes CODATA.
- **Dos vías por clase:** cada laboratorio verifica la solución analítica con una vía numérica o estocástica independiente.
- **Observado frente a ilustrativo:** ningún organismo real se simula con sus parámetros; los valores del laboratorio son sintéticos y se rotulan, y solo se citan con fecha las páginas realmente consultadas (en su mayoría resúmenes obtenidos de Europe PMC).

## 📝 Evaluación del bloque (propuesta, por calibrar)

- Fichas y ejercicios por clase, con retroalimentación y recuperación con evidencia distinta.
- Portafolio: ficha del escalado en frío (C03) y ficha del cultivo en cámara análoga (C07).
- Las condiciones críticas (rotular lo sintético, no presentar un resultado simulado como observado, no proponer cultivos de organismos patógenos y citar solo lo consultado) no se compensan con promedio.

## ⚠️ Seguridad y límites

El bloque es educativo. Los modelos son simplificados y no representan a ninguna cepa concreta. C07 trata solo organismos no patógenos de nivel de bioseguridad 1 y no sustituye a la formación, la aprobación institucional ni los protocolos de un laboratorio real; no se dan instrucciones para manipular muestras ambientales ni organismos que puedan causar daño. Ninguna clase afirma que exista vida fuera de la Tierra.

## Roles que lo usan

- [Astroquímica y astrobiología](../../rutas/astroquimica-y-astrobiologia.md)

## Fuentes de orientación preliminar

- **[NIST-CODATA]** [NIST Fundamental Physical Constants (CODATA 2022)](https://physics.nist.gov/cuu/Constants/Table/allascii.txt) — Constantes físicas fundamentales.
- **[Europe PMC]** [Europe PMC](https://europepmc.org/) — Índice de literatura biomédica y microbiológica usado para localizar los artículos de las clases.
- **[NASA-NSSDC]** [NASA NSSDC Mars Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html) — Presión y composición de la atmósfera marciana.

> La asociación de estas fuentes es orientativa por bloque. Las fuentes realmente consultadas para cada afirmación se registran en la sección 11 de cada clase.

[🏠 Volver al programa](../../README.md) · [⬅️ B63 — Exploración in situ y análisis de muestras planetarias](./B63-exploracion-in-situ-y-analisis-de-muestras-planetarias.md) · [➡️ B65 — Geofísica de interiores planetarios](./B65-geofisica-de-interiores-planetarios.md)
