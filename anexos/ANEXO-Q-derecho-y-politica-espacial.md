# Anexo Q · Derecho, política y sostenibilidad espacial

[⬅️ Anexo P](ANEXO-P-propulsion-y-cohetes.md) · [Índice de anexos](README.md)

**Para qué sirve.** Explica **las reglas del juego** que acompañan a cualquier misión: quién puede hacer qué en el espacio, quién responde si algo sale mal, cómo se reparte el espectro y las órbitas, y qué se hace con la basura espacial. Muchos proyectos fallan o se retrasan no por la ingeniería sino por el permiso, la licencia o la responsabilidad. Este anexo acompaña a los bloques B118 a B123.

> **Estado del texto.** Síntesis propia con fines educativos, pendiente de revisión jurídica y disciplinar (nivel E0). **No es asesoría legal.** Los tratados, normas nacionales y cifras cambian: consulta siempre el texto oficial vigente (Naciones Unidas, UIT, la autoridad de tu país) antes de decidir.

---

## 1. Por qué existe el derecho espacial

El 4 de octubre de 1957 el Sputnik pasó por encima de todos los países sin pedir permiso. De inmediato surgieron preguntas: ¿es el espacio de alguien?, ¿quién responde si cae un satélite?, ¿se pueden poner armas allí? La respuesta fue construir, durante la Guerra Fría, un marco internacional **breve y de principios generales**, que hoy se aplica a una actividad que ya no es solo estatal.

---

## 2. El marco internacional: los cinco tratados de la ONU

| Tratado | Año | Idea central |
|---|---|---|
| **Tratado del Espacio Exterior** | 1967 | Principios básicos (ver 2.1) |
| **Acuerdo de Salvamento** | 1968 | Auxiliar y devolver astronautas y objetos |
| **Convenio de Responsabilidad** | 1972 | El Estado de lanzamiento responde de los daños |
| **Convenio de Registro** | 1975 | Registrar los objetos lanzados y comunicarlo a la ONU |
| **Acuerdo de la Luna** | 1979 | Los recursos lunares son «patrimonio común»; muy pocos Estados lo ratificaron |

### 2.1 Los principios del Tratado del Espacio Exterior
1. **Libre acceso y uso** por todos los Estados, en beneficio de la humanidad.
2. **No apropiación:** el espacio, la Luna y los cuerpos celestes no pueden ser objeto de soberanía nacional.
3. **Se aplica el derecho internacional**, incluida la Carta de la ONU.
4. **Uso pacífico:** prohíbe poner armas nucleares o de destrucción masiva en órbita o en cuerpos celestes; la Luna y otros cuerpos solo para fines pacíficos.
5. **Responsabilidad del Estado** por las actividades de sus nacionales, incluidas las privadas, que requieren autorización y supervisión continua.
6. **Responsabilidad por daños** y jurisdicción sobre los objetos registrados.
7. **Evitar la contaminación nociva** de los cuerpos celestes y del medio terrestre.

**Lección:** no prohíbe toda actividad militar (los satélites de observación y navegación militar son legales); prohíbe ciertas armas y la apropiación.

📘 [B119](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md "Derecho, seguridad y geopolítica espacial"), [B123](../programa/tronco-comun/B123-responsabilidad-danos-y-controversias-espaciales.md "Responsabilidad, daños y controversias espaciales").

---

## 3. Responsabilidad: quién paga cuando algo sale mal

### 3.1 El «Estado de lanzamiento»
Es responsable el Estado que (1) lanza el objeto, (2) hace lanzar el objeto, (3) desde cuyo territorio se lanza o (4) desde cuyas instalaciones se lanza. Un mismo satélite puede tener **varios Estados de lanzamiento**.

### 3.2 Los dos regímenes
- **Daños en la superficie terrestre o a aeronaves en vuelo:** responsabilidad **absoluta**, sin necesidad de probar culpa.
- **Daños en el espacio:** responsabilidad **por culpa** (hay que probar la negligencia del otro).

### 3.3 Un caso real: Cosmos 954 (1978)
Un satélite soviético con un reactor nuclear a bordo reentró y esparció restos radiactivos sobre el norte de Canadá. Canadá reclamó los costos de limpieza (≈ 6 millones de dólares canadienses) con base en la responsabilidad absoluta; la URSS pagó una parte (≈ 3 millones) en un acuerdo de 1981. Es el único caso de reclamación formal con el Convenio.

### 3.4 Ejercicio de aplicación
*Una universidad chilena desarrolla un CubeSat que se lanza en un cohete de una empresa estadounidense desde Nueva Zelanda.* ¿Cuáles son los Estados de lanzamiento? **Respuesta:** Estados Unidos (hace lanzar/lanza), Nueva Zelanda (territorio y/o instalaciones) y, según el contrato y quién «hace lanzar» el objeto, posiblemente Chile. Se registra como mínimo en uno de ellos y debe haber autorizaciones nacionales y seguros.

📘 [B123](../programa/tronco-comun/B123-responsabilidad-danos-y-controversias-espaciales.md "Responsabilidad, daños y controversias espaciales"), [B121](../programa/tronco-comun/B121-regulacion-nacional-de-actividades-espaciales.md "Regulación nacional de actividades espaciales"), [B127](../programa/tronco-comun/B127-seguros-espaciales.md "Seguros espaciales").

---

## 4. Recursos escasos: espectro y órbitas

### 4.1 Espectro radioeléctrico
Los satélites comunican por radio; las frecuencias son un recurso limitado compartido con la telefonía, la aviación y la radioastronomía. La **UIT** (Unión Internacional de Telecomunicaciones) coordina:
- La **asignación de bandas** por servicio.
- La **coordinación y registro** de redes satelitales, para evitar interferencias.
- Plazos para **poner en uso** las frecuencias reservadas (para evitar «satélites de papel»).

### 4.2 Órbitas
La órbita geoestacionaria es un anillo único a 35 786 km: con una separación mínima de ≈ 2°, caben unos 180 satélites; las posiciones se coordinan por la UIT. Las órbitas bajas se llenan con constelaciones de miles de satélites, lo que plantea nuevos problemas de coordinación, de tráfico y de astronomía.

**Ejercicio.** ¿Qué distancia separa a dos satélites geoestacionarios vecinos a 2°? *Solución:* 2° × π/180 × 42 164 km ≈ **1 470 km**. Comprobación: `calc "radians(2)*42164"`.

📘 [B120](../programa/tronco-comun/B120-espectro-licencias-y-regulacion-satelital.md "Espectro, licencias y regulación satelital"), [B89](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md "Comunicaciones y navegación satelital"), [B91](../programa/tronco-comun/B91-antenas-y-propagacion-para-enlaces-espaciales.md "Antenas y propagación para enlaces espaciales").

---

## 5. Basura espacial y sostenibilidad

### 5.1 El problema
Millones de fragmentos orbitan la Tierra; decenas de miles se rastrean (los mayores de ≈ 10 cm). A velocidades relativas de hasta ≈ 15 km/s, un objeto pequeño es peligroso.

**Ejercicio.** Energía de una esfera de aluminio de 1 cm (≈ 1,4 g) a 10 km/s. *Solución:* ½ × 1,4 × 10⁻³ × (10⁴)² ≈ **70 kJ**, comparable a una bola de boliche de 7 kg a ≈ 510 km/h. Comprobación: `calc "0.5*1.4e-3*1e4**2"`.

### 5.2 Eventos que marcaron la agenda
- **2007:** China destruyó con un misil su satélite Fengyun-1C: miles de fragmentos rastreables, muchos de larga vida.
- **2009:** colisión accidental entre Iridium 33 y Cosmos 2251.
- **2021:** Rusia destruyó Cosmos 1408 en otra prueba antisatélite; en 2022 la Asamblea General de la ONU adoptó una resolución para una moratoria de ese tipo de pruebas.

### 5.3 Reglas de buenas prácticas
- **Directrices del IADC** (comité entre agencias): limitar los residuos liberados, evitar la fragmentación, **desorbitar** al final de la vida.
- **Regla de los 25 años:** un satélite en LEO debe reentrar en un máximo de 25 años; algunos reguladores (por ejemplo, Estados Unidos desde 2022) exigen 5 años.
- **Directrices de largo plazo de la ONU (2019):** 21 directrices sobre la sostenibilidad de las actividades espaciales.
- **GEO:** mover el satélite a una órbita «cementerio» unos cientos de km por encima.

### 5.4 Conflicto con la astronomía
Las grandes constelaciones dejan trazas en las imágenes de los telescopios y elevan el brillo del cielo. Hay mitigaciones (oscurecer, ajustar orientación, coordinar con observatorios), pero el problema es abierto y afecta especialmente a Chile, que alberga gran parte de la astronomía mundial.

📘 [B118](../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md "Tráfico espacial y sostenibilidad orbital"), [B119](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md "Derecho, seguridad y geopolítica espacial").

---

## 6. Recursos espaciales: una cuestión abierta

¿Se puede extraer agua de la Luna o minerales de un asteroide y quedarse con ellos? Hay dos lecturas:
- **Extraer no es apropiarse del cuerpo:** como la pesca en alta mar, se puede aprovechar el recurso extraído sin reclamar soberanía. Es la posición de leyes nacionales como las de Estados Unidos (2015), Luxemburgo (2017), Emiratos Árabes Unidos (2019) y Japón (2021).
- **Hace falta un régimen internacional:** el espacio es «patrimonio común», como defiende el Acuerdo de la Luna.

Los **Acuerdos Artemis** (2020) son compromisos políticos no vinculantes, impulsados por Estados Unidos, que incluyen principios sobre transparencia, interoperabilidad y extracción de recursos; más de cincuenta países los han firmado. Otros países prefieren negociar en la ONU.

**Lección:** el derecho aún no zanjó este tema; el debate refleja intereses distintos.

📘 [B59](../programa/tronco-comun/B59-recursos-in-situ-y-sostenibilidad-extraterrestre.md "Recursos in situ y sostenibilidad extraterrestre"), [B67](../programa/tronco-comun/B67-prospeccion-y-evaluacion-de-reservas-de-recursos-extraterrestres.md "Prospección y evaluación de reservas de recursos extraterrestres"), [B119](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md "Derecho, seguridad y geopolítica espacial").

---

## 7. Seguridad y uso militar

- Los satélites militares de comunicación, navegación y reconocimiento son legales y hoy esenciales en la vida civil: **el GPS nació como sistema militar**.
- Se discuten las armas antisatélite, los ataques cibernéticos a satélites y la interferencia (jamming).
- Existen fuerzas armadas con rama espacial (por ejemplo, la Fuerza Espacial de Estados Unidos, creada en 2019).
- Un **ataque a infraestructura espacial** puede afectar a servicios civiles (cajeros, aviación, energía): de ahí el interés por la **resiliencia**.

📘 [B119](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md "Derecho, seguridad y geopolítica espacial"), [B122](../programa/tronco-comun/B122-resiliencia-y-continuidad-de-infraestructura-espacial.md "Resiliencia y continuidad de infraestructura espacial").

---

## 8. Ética y equidad

- **Acceso equitativo:** países sin capacidad propia dependen de otros para lanzar y para datos; los CubeSats y los datos abiertos reducen esa brecha.
- **Protección planetaria:** no contaminar otros mundos y proteger la Tierra de muestras traídas (COSPAR).
- **Patrimonio cultural:** hay sitios de valor histórico en la Luna (Mar de la Tranquilidad) que se discute proteger.
- **Cielo oscuro y saberes locales:** el cielo es patrimonio de pueblos que lo leen desde hace milenios; observatorios y constelaciones afectan su relación con el territorio ([Anexo S](ANEXO-S-chile-y-cielos-originarios.md)).

📘 [B119](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md "Derecho, seguridad y geopolítica espacial"), [B133](../programa/tronco-comun/B133-saberes-astronomicos-y-educacion-intercultural.md "Saberes astronómicos y educación intercultural").

---

## 9. Cómo se otorga la licencia a una misión

1. **Autorización nacional** del lanzamiento y de la operación (autoridad espacial o de telecomunicaciones).
2. **Licencia de frecuencias** (autoridad nacional y coordinación UIT).
3. **Evaluación ambiental y de basura espacial** (plan de fin de vida).
4. **Seguros** de responsabilidad hacia terceros.
5. **Registro** del objeto y comunicación a la ONU.
6. **Control de exportaciones** si hay tecnología sensible.

**Ejercicio de planificación.** Para el CubeSat universitario del ejercicio 3.4, ordena los seis pasos, estima qué documentos pedirías a la universidad y qué parte del trámite suele demorar más. *Respuesta típica:* las frecuencias y la autorización de lanzamiento; conviene empezar 12–18 meses antes del lanzamiento.

📘 [B120](../programa/tronco-comun/B120-espectro-licencias-y-regulacion-satelital.md "Espectro, licencias y regulación satelital"), [B121](../programa/tronco-comun/B121-regulacion-nacional-de-actividades-espaciales.md "Regulación nacional de actividades espaciales"), [B127](../programa/tronco-comun/B127-seguros-espaciales.md "Seguros espaciales").

---

## 10. Preguntas para discutir

1. ¿Por qué el Tratado del Espacio Exterior prohíbe la soberanía, pero la extracción de recursos se discute?
2. ¿Quién debería responder por los daños de una constelación privada?
3. ¿Qué responsabilidad tiene un país que solo ofrece el territorio para un lanzamiento?
4. ¿Cómo se puede equilibrar la expansión de las constelaciones con la astronomía?

[⬅️ Anexo P](ANEXO-P-propulsion-y-cohetes.md) · [Índice de anexos](README.md)
