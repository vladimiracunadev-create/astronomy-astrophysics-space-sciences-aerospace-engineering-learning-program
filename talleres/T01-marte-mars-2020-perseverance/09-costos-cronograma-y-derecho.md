# Capítulo 9 · Costos, cronograma, derecho y cooperación

## Por qué existe este capítulo

Una misión técnicamente perfecta que no cabe en el presupuesto o que pierde la ventana de lanzamiento **no vuela**. Este capítulo reúne el dinero, el tiempo y las reglas: lo que decide si el diseño de los capítulos anteriores llega a existir.

## Costo: lo que se sabe y lo que no

Cifras públicas de referencia para Mars 2020 (redondeadas, ⚠ contrasta con la fuente de la NASA):

- **Costo total del ciclo de vida:** del orden de **2.700 millones de dólares**, incluyendo desarrollo, lanzamiento y operaciones de la misión primaria.
- **Servicio de lanzamiento:** ≈ **243 millones**.
- **Herencia:** reutilizar el diseño de Curiosity redujo el costo de desarrollo (no se rehízo la arquitectura de entrada y descenso).

### Estructura de desglose del trabajo (WBS)

Todo proyecto desglosa su costo por **áreas de trabajo**: gestión, ingeniería de sistemas, ciencia, carga útil (instrumentos), vehículo, lanzamiento, operaciones de misión, protección planetaria, seguridad. Cada área tiene responsable, presupuesto y calendario.

### Reservas

Un presupuesto realista incluye **reservas**, decididas por la madurez de cada pieza:

- Hasta ≈ **30 %** al inicio, cuando hay más incertidumbre.
- Menor al avanzar, pero **nunca cero** hasta el lanzamiento.
- La reserva se gestiona por el director del proyecto, no por cada ingeniero.

El laboratorio (sección 7) calcula un ejemplo ilustrativo: un subtotal de ≈ 2.090 millones más un 30 % de reserva da ≈ 2.720 millones, del orden del costo publicado. **El reparto interno de ese ejemplo es ilustrativo**; el estudiante debe usar su propia fuente.

### Qué se encarece

- **Cambios tardíos de requisitos.** Cuanto más tarde se descubre un cambio, más cuesta.
- **Retrasos en la entrega de piezas** o en las pruebas, que arrastran al equipo entero.
- **Perder la ventana.** Si se pierde, se espera ≈ 26 meses con el equipo y la nave guardados: esa espera cuesta cientos de millones. Mars 2020 estuvo muy cerca de verse afectada por problemas de pruebas y luego por las restricciones de la pandemia de 2020; se logró lanzar dentro de la ventana (⚠ contrasta los detalles).

## Cronograma

Una misión interplanetaria tiene un **calendario atado a la ventana**. Hitos típicos (los plazos son orientativos):

| Fase | Qué se hace | Duración orientativa |
|---|---|---|
| A · Concepto | Objetivos, estudios de viabilidad | 1-2 años |
| B · Diseño preliminar | Requisitos, arquitectura, PDR | 1-2 años |
| C · Diseño final y construcción | CDR, fabricación de las piezas | 2-3 años |
| D · Integración, pruebas y lanzamiento | Ensamblaje, vacío térmico, vibración, campaña de lanzamiento | 1-2 años |
| E · Operaciones | Crucero, llegada y misión primaria | ≈ 7 meses de viaje + 1 año marciano o más |
| F · Cierre | Fin de misión y disposición | según el caso |

El **camino crítico** es la cadena de tareas sin holgura: cualquier retraso en ella retrasa todo. Se identifica y se vigila cada semana.

## Cooperación internacional

Las misiones a Marte rara vez son de un solo país. Mars 2020 incluyó contribuciones de **otros países y agencias** (por ejemplo, instrumentos con participación de instituciones europeas, españolas y de otros países; ⚠ verificar la lista). La cooperación aporta capacidades y repartos de costo, pero **añade interfaces**, y las interfaces son una fuente clásica de errores (ver el Mars Climate Orbiter, capítulo 7). La regla: cada interfaz tiene un documento de control con unidades y sistemas de referencia explícitos, y un responsable de cada lado.

El programa de **retorno de muestras** (Mars Sample Return) pensaba reunir a la NASA y a la ESA; su arquitectura, costo y calendario han cambiado, y es un buen caso para estudiar cómo se **rediseña un programa** cuando los costos crecen (⚠ consulta el estado actual).

## Marco legal

- **Tratado del Espacio Ultraterrestre (1967):** el espacio no se puede apropiar; los Estados son responsables de sus actividades, incluidas las de empresas privadas; se debe evitar la contaminación nociva.
- **Convenio sobre responsabilidad (1972):** un Estado de lanzamiento es **responsable de los daños** causados por sus objetos espaciales, y de forma **absoluta** si caen en la superficie terrestre o en un avión en vuelo.
- **Convenio de registro (1975):** los objetos lanzados se registran ante la ONU.
- **Normas de radiofrecuencia (UIT):** las frecuencias de comunicación se coordinan internacionalmente.
- **Control de exportaciones:** la tecnología espacial puede tener restricciones de transferencia entre países (reglamentos nacionales; para Estados Unidos, por ejemplo, ITAR/EAR).
- **Licencias y seguros:** el lanzamiento exige autorización nacional y, en algunos casos, seguro de responsabilidad.

## Ejercicio del capítulo

1. Haz tu **WBS** de primer nivel y asigna un porcentaje de costo a cada rama; justifícalo.
2. Calcula tu costo total con **reservas distintas** (20 %, 30 %, 40 %). ¿Qué ocurre con la decisión de «ir o no ir» si el tope del proyecto es fijo?
3. Dibuja un **cronograma** de 8 años con las fases A a F y marca el **camino crítico**. ¿Qué pasa si una prueba se retrasa seis meses?
4. Lista las **interfaces** con otras agencias o empresas de tu misión y escribe qué debe decir el documento de control de cada una.
5. Redacta un párrafo sobre **responsabilidad legal** en tu lanzamiento: ¿qué Estado responde y de qué?

Anterior: [capítulo 8](08-proteccion-planetaria-y-seguridad.md) · Siguiente: [capítulo 10 · Entregables y rúbrica](10-entregables-y-rubrica.md)
