# Anexo T · Dónde están los datos: fuentes, archivos y herramientas

[⬅️ Anexo S](ANEXO-S-chile-y-cielos-originarios.md) · [Índice de anexos](README.md)

**Para qué sirve.** Un programa de astronomía y de ciencias espaciales se aprende de verdad cuando se trabaja con **datos reales**: imágenes, espectros, órbitas, catálogos. Este anexo dice **dónde están**, **en qué formato vienen**, **cómo se citan** y **qué precauciones tomar**, y propone un primer proyecto con datos que puedes hacer tú. No reemplaza al estándar de fuentes del repositorio ([`documentacion/ESTANDAR_DE_FUENTES.md`](../documentacion/ESTANDAR_DE_FUENTES.md)): lo complementa con una guía práctica.

> **Estado del texto.** Síntesis propia, pendiente de revisión (nivel E0). Los nombres y las direcciones de los servicios cambian: **verifica siempre el enlace oficial** de cada agencia antes de usarlo; este anexo no reproduce el contenido de ninguno de ellos. Respeta las licencias y las condiciones de uso de cada archivo.

---

## 1. Antes de buscar: cuatro preguntas

1. **¿Qué quiero medir o responder?** (una pregunta clara evita descargar de más).
2. **¿Qué tipo de dato necesito?** (imagen, espectro, serie de tiempo, órbita, catálogo, telemetría).
3. **¿Qué nivel de procesamiento?** (cruda, calibrada, producto científico). Empieza por los productos calibrados.
4. **¿Qué licencia y qué cita exige?** (la mayoría de los datos de agencias son abiertos, con petición de agradecimiento).

---

## 2. Mapa de fuentes por tipo de dato

| Necesito… | Dónde buscar (tipo de servicio) | Ejemplos de contenido |
|---|---|---|
| **Datos de misiones planetarias** | Archivos de datos planetarios de las agencias (NASA PDS, ESA PSA) | Imágenes de rovers, espectros, mapas de sondas |
| **Imágenes y espectros de telescopios espaciales** | Archivos de misión (MAST, archivos de ESA) | Hubble, JWST, Kepler, TESS, Gaia |
| **Catálogos de estrellas y galaxias** | Servicios del Observatorio Virtual (VizieR, SIMBAD, archivos de Gaia) | Posiciones, magnitudes, paralajes |
| **Exoplanetas** | Archivos de exoplanetas (NASA Exoplanet Archive, Enciclopedia de Exoplanetas) | Parámetros de más de 5 800 planetas |
| **Observatorios en Chile** | Archivos de ESO, NOIRLab (Gemini, CTIO), ALMA, Rubin | Datos científicos públicos tras el período de propiedad |
| **Órbitas de satélites** | Elementos de dos líneas (TLE) y servicios de seguimiento | Posición de satélites y basura |
| **Efemérides del Sistema Solar** | Sistemas de efemérides (JPL Horizons) | Posición de planetas, lunas, asteroides |
| **Clima espacial** | Centros de predicción (NOAA SWPC) | Viento solar, índice Kp, llamaradas |
| **Observación de la Tierra** | Programas Landsat, Copernicus (Sentinel) | Imágenes multiespectrales y de radar |
| **Constantes y unidades** | Organismos de metrología (CODATA/NIST, UAI, BIPM) | Valores y resoluciones oficiales |

**Prioridad de confianza:** (1) datos y documentación de la propia misión; (2) artículos científicos revisados por pares; (3) revisiones y libros de texto; (4) fuentes divulgativas. Una fuente divulgativa puede orientar, **no** respaldar una decisión técnica.

📘 [B14](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md "Computación científica y ciencia abierta"), [B20](../programa/tronco-comun/B20-metodologia-de-la-investigacion-cientifica.md "Metodología de la investigación científica"), [B23](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md "Verificación y validación de software científico").

---

## 3. Formatos de datos que encontrarás

| Formato | Para qué se usa | Cómo se lee |
|---|---|---|
| **FITS** | Imágenes y espectros astronómicos con cabecera descriptiva | Bibliotecas como Astropy |
| **CSV / ASCII** | Tablas simples | Cualquier programa |
| **VOTable** | Tablas del Observatorio Virtual | Herramientas del Observatorio Virtual |
| **HDF5 / NetCDF** | Grandes arreglos científicos (clima, simulaciones) | Bibliotecas específicas |
| **PDS4 / PDS3** | Archivos planetarios con metadatos | Herramientas de las agencias |
| **SPICE kernels** | Geometría de misiones (posición, orientación, tiempo) | Biblioteca SPICE |
| **TLE** | Elementos orbitales de dos líneas | Propagadores (SGP4) |
| **GeoTIFF / JPEG2000** | Imágenes georreferenciadas | Herramientas GIS |

**La cabecera importa.** Un archivo FITS trae en su cabecera el instrumento, la fecha (¿UTC? ¿JD?), las unidades, la calibración y el sistema de coordenadas. **Léela siempre**; una imagen sin su cabecera es una imagen sin contexto.

---

## 4. Buenas prácticas con datos

### 4.1 Trazabilidad
Anota para cada dato: **fuente, fecha de descarga, versión, identificador del producto y procesamiento aplicado**. Si no puedes reproducir de dónde vino, no puedes defender el resultado.

### 4.2 Unidades y marcos
Antes de calcular, verifica **unidades**, **escala de tiempo** (UTC, TAI, TT, TDB), **marco de referencia** (ICRS, ecuatorial, eclíptico) y **época**. Muchas discrepancias entre cálculos vienen de aquí (ver el [Anexo I](ANEXO-I-escalas-formulas-y-calculadora.md) y el caso del [Mars Climate Orbiter](ANEXO-J-estudios-de-caso-a-fondo.md)).

### 4.3 Incertidumbre
Todo dato tiene incertidumbre. Busca la que reporta la fuente (error, desviación estándar, nivel de confianza) y **propágala**. Un resultado sin incertidumbre no es un resultado completo.

### 4.4 Datos faltantes y sesgos
Revisa si hay valores nulos, saturación, satélites o rayos cósmicos en las imágenes, y sesgos de selección (¿qué objetos se ven y cuáles no?).

### 4.5 Reproducibilidad
Guarda el **código**, el **entorno** (versiones de bibliotecas) y los **parámetros**. Un notebook que funciona solo en tu equipo no es reproducible.

📘 [B14](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md "Computación científica y ciencia abierta"), [B15](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md "Señales, imágenes y estimación científica"), [B23](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md "Verificación y validación de software científico").

---

## 5. Cómo citar

Un buen registro (siguiendo el estándar de fuentes del repositorio) incluye:
- Autor u organismo y título del dato o artículo.
- Versión, edición o fecha de publicación.
- Identificador persistente (DOI, bibcode) o enlace oficial.
- Fecha de consulta (si el recurso cambia).
- Qué afirmación respalda.
- Licencia o condiciones de uso.

**Regla de oro:** no cites una página de resultados de búsqueda como fuente final; cita el recurso concreto.

---

## 6. Herramientas de trabajo

| Tarea | Herramienta típica | Nota |
|---|---|---|
| Cálculos rápidos y conversión de unidades | La [calculadora del programa](../herramientas/calculadora_cientifica.py) | Solo biblioteca estándar |
| Lectura y análisis de datos | Python con bibliotecas científicas (NumPy, SciPy, Astropy, Matplotlib) | Instalar en un entorno aislado y con versiones fijas |
| Propagación de órbitas | Bibliotecas de SGP4 y de mecánica orbital | Para fines educativos |
| Visualización del cielo | Planetarios de código abierto | Útiles para ubicar objetos |
| Procesamiento de imágenes | Herramientas de reducción astronómica | Aplicar sesgo, oscuro y campo plano |
| Control de versiones | Git | Guardar código y notas |

---

## 7. Un primer proyecto con datos reales

**Objetivo.** Medir el período de una estrella variable o de un exoplaneta en tránsito con datos públicos.

**Pasos.**
1. Elige un objeto conocido (por ejemplo, una binaria eclipsante brillante o un Júpiter caliente con curva de luz pública).
2. Descarga la **curva de luz** desde un archivo de misión (TESS, por ejemplo) y lee su cabecera.
3. Convierte los tiempos a una escala común y quita los valores inválidos.
4. Calcula el **periodograma** (frecuencia con más potencia) para estimar el período.
5. Pliega la curva de luz con ese período y mide la profundidad del tránsito.
6. Calcula el radio del planeta con δ = (R_p/R_*)² y compáralo con un valor publicado.
7. Estima la incertidumbre y escribe la **ficha de resultado**: datos, método, resultado, error, limitaciones.

**Criterios de evaluación.** (a) trazabilidad completa; (b) unidades y escalas de tiempo explícitas; (c) incertidumbre calculada; (d) comparación con la literatura; (e) código reproducible.

📘 [B15](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md "Señales, imágenes y estimación científica"), [B29](../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md "Astronomía temporal y exoplanetas"), [B14](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md "Computación científica y ciencia abierta"), [B20](../programa/tronco-comun/B20-metodologia-de-la-investigacion-cientifica.md "Metodología de la investigación científica").

---

## 8. Preguntas para estudiar

1. ¿Por qué un dato calibrado puede ser mejor para empezar que uno crudo?
2. ¿Qué información de una cabecera FITS es imprescindible antes de analizar una imagen?
3. ¿Qué diferencia hay entre repetir un cálculo y reproducir un análisis?
4. ¿Qué se pierde al citar una página divulgativa en lugar del artículo original?

[⬅️ Anexo S](ANEXO-S-chile-y-cielos-originarios.md) · [Índice de anexos](README.md)
