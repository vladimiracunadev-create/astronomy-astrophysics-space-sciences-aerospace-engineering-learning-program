# Guía de recorridos por rol

Cada una de las 24 rutas profesionales es un **rol**. Un rol no cursa «160 clases propias y todo lo demás»: usa **unas clases concretas del tronco común y de su ruta, en un orden con sentido**. Este documento fija cómo se define, se valida y se mantiene ese recorrido.

## Qué cambia respecto del catálogo plano

El catálogo `0.1.0` da a todas las rutas el mismo tamaño (8 módulos × 20 clases). El recorrido corrige esa simetría desde el uso: dos roles pueden compartir el tronco común y, aun así, usar clases distintas, en distinto orden y con distinto peso. El número de clases de un recorrido no tiene por qué coincidir con el de otro.

## Fuente de verdad y herramientas

- `metadatos/recorridos/Rxx.json`: un archivo por ruta (así varias personas pueden editar roles distintos sin conflictos). Estado `definido` o `pendiente`.
- `herramientas/validar_recorridos.py`: valida estructura y existencia de cada ID contra el catálogo.
- `herramientas/generar_recorridos.py`: genera `programa/rutas-profesionales/<ruta>/RECORRIDO.md` a partir del JSON (no se edita a mano) y enlaza el recorrido en el `INDICE.md` de la ruta. `--check` falla si algo está desactualizado.

## Campos de un rol definido

| Campo | Contenido |
|---|---|
| `rol` | Nombre del rol en lenguaje de trabajo. |
| `resumen` | Qué hace la persona en una frase concreta. |
| `decide` | Qué decide: lo que distingue este rol de los vecinos. |
| `entrega` | Qué produce y deja como evidencia. |
| `pasos` | Lista ordenada (campo `orden` consecutivo desde 1). |
| `modulos` | Los 8 módulos de la ruta y, para cada uno de sus 10 temas (pares de clases C01..C02, …, C19..C20), dónde vive su contenido: `existente` (IDs del tronco) o `nueva` (propuesta de clase con área, bloque y título). Los módulos no duplican contenido. |
| `huecos` | Temas que el rol necesita y el catálogo no cubre (lista; puede ser vacía). |

Cada **paso** tiene: `fase` (`fundamentos`, `tronco`, `ruta`, `integracion`), `tipo` (`obligatoria`, `recomendada`, `opcional`), `titulo`, `clases`, `capacidad` (qué puede hacer la persona al terminarlo; mínimo una frase), y opcionalmente `nota` y `omitible_si` (la evidencia o diagnóstico que permite saltarlo).

`clases` acepta IDs sueltos (`B01-C08`) y rangos dentro de un mismo bloque o módulo (`B83-C01..C20`, `R12-M04-C01..C20`).

## Reglas

1. **Capacidad, no bloque entero.** Se eligen clases por la capacidad que aportan. Si se omiten clases de un bloque, la `nota` dice cuáles y por qué.
2. **Orden con sentido.** Los fundamentos van primero; el tronco aplicado y los módulos de la ruta pueden intercalarse (por ejemplo, un módulo de potencia después del bloque de potencia); la integración va al final.
3. **Sin repeticiones.** Una clase aparece una sola vez por rol.
4. **Cobertura de la ruta.** Los pasos incluyen todas las clases del tronco que el mapa `modulos` asigna a los módulos, y los IDs de ruta (`Rxx-Mxx-Cnn`) solo aparecen como referencia provisional de temas `nueva`. Mientras un rol no tenga `modulos`, el validador lo avisa sin fallar.
5. **Reutilización explícita.** Cuando un módulo de la ruta profundiza un tema que ya vio el tronco, la `nota` lo dice y la clase de la ruta debe pedir una evidencia distinta (ver [plan de refinamiento](PLAN_DE_REFINAMIENTO_CURRICULAR.md), L2).
6. **Diferencias reales.** El validador rechaza dos roles con recorridos casi idénticos (similitud de Jaccard mayor que 0,9).
7. **Diagnóstico antes que obligación.** Los fundamentos llevan `omitible_si` cuando una evidencia demuestra el dominio. Nadie repite lo que ya demuestra.
8. **Huecos honestos.** Si el catálogo no tiene una clase que el rol necesita, no se disimula con una parecida: se registra en `huecos` con el motivo y la propuesta (ver [ampliación del tronco común](AMPLIACION_DEL_TRONCO_COMUN.md)).
9. **Sin promesas profesionales.** Un recorrido no habilita, certifica ni sustituye una titulación (ver [alcance y contrato](ALCANCE_Y_CONTRATO_DEL_REPOSITORIO.md)).

## El documento vinculante del rol

`RECORRIDO.md` de cada ruta es el documento que vincula el proceso: enlaza cada clase en orden (a su página si ya está redactada o a la guía de su bloque) y muestra, módulo por módulo, dónde vive el contenido en el tronco común. Se genera; no se edita a mano.

## Guía del rol

Además del recorrido, cada ruta tiene `GUIA_DEL_ROL.md`, escrita en prosa para quien decide si el rol es para sí: qué es y qué no es (con qué roles vecinos se confunde), un día de trabajo, qué decide y qué entrega, conocimientos y herramientas, evidencias y portafolio, progresión y límites éticos. Cita solo fuentes realmente consultadas, con la misma regla de [estándar de fuentes](ESTANDAR_DE_FUENTES.md).

## Comprobaciones antes de subir

```text
python herramientas/validar_recorridos.py
python herramientas/generar_recorridos.py && python herramientas/generar_recorridos.py --check
python herramientas/validar_catalogo.py
```
