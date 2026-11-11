# Anexo I · Escalas de medición, fórmulas y calculadora científica

[⬅️ Anexo H](ANEXO-H-cronologia.md) · [Índice de anexos](README.md)

Dos personas pueden calcular "lo mismo" y obtener resultados distintos sin que ninguna se haya equivocado: una usó el año juliano y otra el tropical, una el parsec redondeado y otra el definido, una la masa solar medida y otra la nominal. Este anexo reúne **las escalas** que usa el programa, **las fórmulas** que las relacionan y **las convenciones** que hay que fijar antes de comparar cálculos, y acompaña a una **calculadora en Python** para comprobarlos.

> **Estado del texto.** Síntesis propia, pendiente de revisión disciplinar y de contraste con las fuentes citadas (nivel E0). Los valores de las constantes provienen de CODATA 2018, de las resoluciones de la UAI 2012 y 2015 y de las definiciones del SI 2019; las constantes que dependen de ellas se calculan en el código. Antes de usar un valor en un trabajo, cita su fuente y versión.

---

## 1. La calculadora

Archivo: [`herramientas/calculadora_cientifica.py`](../herramientas/calculadora_cientifica.py). Solo usa la biblioteca estándar de Python (no instala nada). Cada resultado declara sus supuestos.

```bash
python herramientas/calculadora_cientifica.py autotest
```

| Orden | Qué hace | Ejemplo |
|---|---|---|
| `const` | Constante con unidad y fuente | `const G` |
| `convert` | Convierte unidades (longitud, masa, tiempo, energía, ángulo, presión, velocidad, potencia, temperatura) | `convert 1 pc ly` |
| `calc` | Evalúa una expresión con constantes y funciones matemáticas, sin `eval()` | `calc "sqrt(2*GM_tierra/(R_tierra+400e3))"` |
| `modulo-distancia` | m − M = 5 log₁₀(d / 10 pc) | `modulo-distancia --m 5 --M 0` |
| `flujos` | Razón de flujos por diferencia de magnitud | `flujos -5` |
| `orbita` | Periodo, velocidad circular y de escape | `orbita --a 6778e3 --cuerpo tierra` |
| `hohmann` | Transferencia entre órbitas circulares | `hohmann --r1 6678e3 --r2 42164e3` |
| `cohete` | Ecuación de Tsiolkovski | `cohete --isp 450 --m0 1000 --mf 300` |
| `estrella` | Luminosidad y pico de Wien | `estrella --radio 6.957e8 --temp 5772` |
| `fecha-juliana` | Día juliano de una fecha | `fecha-juliana 2000 1 1.5` |
| `autotest` | 20 comprobaciones con valores conocidos y tolerancia declarada | `autotest` |

**Límites:** es una herramienta didáctica. Supone problema de dos cuerpos, órbitas circulares o impulsos instantáneos donde se indica; no incluye perturbaciones, arrastre, relatividad, extinción ni incertidumbres. No sirve para decisiones de vuelo, lanzamiento o seguridad. 📘 [B13](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md "Metrología, tiempo y mediciones científicas"), [B14](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md "Computación científica y ciencia abierta"), [B23](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md "Verificación y validación de software científico").

---

## 2. Dónde los cálculos "no se ponen de acuerdo" y cómo reconciliarlos

| Asunto | Diferencia habitual | Convención del programa | Efecto típico |
|---|---|---|---|
| **Año** | Juliano (365,25 d), tropical (365,2422 d), sidéreo (365,2564 d), calendario (365 d) | Juliano de 365,25 d de 86 400 s para año luz y conversiones | Hasta ~ 0,02 % en tiempos largos |
| **Año luz** | Depende del año | c × 365,25 d = 9,4607 × 10¹⁵ m | Pequeño pero acumulable |
| **Parsec** | Redondeado (3,26 al) o definido | 648 000/π UA (UAI 2015) = 3,0857 × 10¹⁶ m | ~ 0,1 % si se redondea |
| **Unidad astronómica** | Antes dependía de mediciones | Definida exacta: 149 597 870 700 m (UAI 2012) | Ninguno desde 2012 |
| **Masa del Sol** | G M☉ conocida con precisión; M☉ depende de G | Se usa **GM** nominal (UAI 2015) y se evita separar G y M | Error de G (~ 2 × 10⁻⁵) |
| **Radio de la Tierra** | Ecuatorial 6378,1 km, medio 6371,0 km, polar 6356,8 km | Ecuatorial nominal; se indica cuando se usa el medio | ~ 0,3 % en velocidades de escape |
| **Gravedad** | 9,80665 (estándar), 9,81 o 9,8 | g₀ = 9,80665 m/s² para Isp | 0,05–0,1 % |
| **Logaritmo** | log (base 10) y ln (base e) con el mismo nombre | `log10` y `ln` siempre explícitos | Factor 2,3026 |
| **Magnitud estelar** | Signo invertido: más brillante = menor número | m₁ − m₂ = −2,5 log₁₀(F₁/F₂) | Errores de signo |
| **Tiempo** | UTC (segundos intercalares), TAI, TT (= TAI + 32,184 s), TDB | Se declara la escala; TT para efemérides, UTC para civil | Segundos a minutos |
| **Fecha juliana** | JD (inicia a mediodía) y JD modificado (MJD = JD − 2 400 000,5, inicia a medianoche) | Se declara JD o MJD | Medio día de desfase |
| **Ángulos** | Grados, horas (1 h = 15°), radianes | Radianes internos; se convierte al mostrar | Factores de 15 y π/180 |
| **Masa/peso** | Masa (kg) y fuerza (N) | Masa en kg, fuerza en N | Error de g |
| **Temperatura** | K, °C, °F | K en fórmulas físicas | Diferencias de 273,15 |
| **Redondeo** | Cifras significativas distintas | Se informan al menos 3–4 cifras y la tolerancia | Falsas discrepancias |
| **Sistema de unidades** | SI, CGS (erg, dina, gauss), unidades astronómicas | SI; se convierte al mostrar | Factores de 10⁷ o 10⁻⁷ |
| **Marco de referencia** | Heliocéntrico, geocéntrico, topocéntrico | Se declara siempre | Corrección de hasta 20″ (aberración) |

**Regla práctica:** antes de comparar dos cálculos, anota constantes, unidades, marco de referencia, escala de tiempo y cifras significativas. Si coinciden, la diferencia viene de otra parte. 📘 [B13](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md "Metrología, tiempo y mediciones científicas"), [B12](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md "Probabilidad, estadística e incertidumbre"), [B23](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md "Verificación y validación de software científico").

---

## 3. Escalas de distancia y tamaño

| Escala | Valor de referencia | Para qué sirve |
|---|---|---|
| Radio terrestre ecuatorial | 6 378,1 km (nominal) | Altitud orbital |
| Distancia Tierra–Luna | ≈ 384 400 km (media) | Comunicaciones: ≈ 1,28 s de luz |
| Unidad astronómica | 149 597 870 700 m | Sistema solar; ≈ 499 s de luz |
| Año luz | ≈ 9,4607 × 10¹⁵ m | Estrellas cercanas |
| Parsec | ≈ 3,0857 × 10¹⁶ m = 3,2616 al | Distancias galácticas |
| kpc, Mpc, Gpc | 10³, 10⁶, 10⁹ pc | Galaxia, cúmulos, cosmología |

**Escalera de distancias (idea):** paralaje (hasta ~ kpc) → cefeidas y RR Lyrae → supernovas tipo Ia → ley de Hubble. Cada peldaño se calibra con el anterior, y el error se propaga. 📘 [B25](../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md "Galaxias y medio interestelar"), [B26](../programa/tronco-comun/B26-relatividad-y-cosmologia.md "Relatividad y cosmología").

**Fórmulas básicas**
- Paralaje: d [pc] = 1 / p [arcsec].
- Módulo de distancia: m − M = 5 log₁₀(d / 10 pc) (sin extinción; con ella, + A_λ).
- Ley de Hubble (z pequeño): v ≈ H₀ d, con H₀ ≈ 70 km s⁻¹ Mpc⁻¹; el valor exacto depende del método y es objeto de debate (tensión de Hubble).

---

## 4. Escalas de brillo, color y flujo

- **Magnitud aparente (m)** y **absoluta (M, a 10 pc)**; escala logarítmica donde 5 magnitudes = factor 100 en flujo.
- **Pogson:** F₁ / F₂ = 10^(−0,4 (m₁ − m₂)); 1 mag ≈ 2,512.
- **Índice de color:** B − V (por ejemplo, el Sol ≈ 0,65).
- **Luminosidad bolométrica:** M_bol☉ ≈ 4,74 (convención UAI 2015).
- **Flujo espectral:** 1 Jy = 10⁻²⁶ W m⁻² Hz⁻¹ (radioastronomía).
- **Brillo superficial del cielo:** mag/arcsec² (a mayor número, más oscuro).
- **Escala de Bortle (1 a 9):** cielo oscuro (1) a ciudad (9), según estrellas visibles a simple vista y aspecto de la Vía Láctea.

📘 [B24](../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md "Física y evolución de estrellas"), [B45](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md "Espectroscopía, fotometría y polarimetría"), [B44](../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md "Detectores y adquisición astronómica").

---

## 5. Escalas de tiempo

| Escala | Qué es | Uso |
|---|---|---|
| UTC | Tiempo civil con segundos intercalares | Operación, registros |
| TAI | Tiempo atómico internacional (continuo) | Metrología |
| TT | Tiempo terrestre = TAI + 32,184 s | Efemérides |
| TDB | Tiempo dinámico baricéntrico | Dinámica del sistema solar |
| GPS | Continuo, = TAI − 19 s | Navegación |
| JD / MJD | Días continuos desde −4712 / desde 1858-11-17 | Cálculo y archivo de datos |
| Tiempo sidéreo | Basado en la rotación respecto a estrellas | Pone un objeto en el meridiano |

Equivalencia exacta: MJD = JD − 2 400 000,5. El día J2000.0 corresponde a JD 2 451 545,0 (1 de enero de 2000, 12:00 TT). 📘 [B13](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md "Metrología, tiempo y mediciones científicas").

---

## 6. Escalas de energía, temperatura y potencia

- **Temperatura:** K = °C + 273,15; °F = °C × 9/5 + 32.
- **Energía de un fotón:** E = h c / λ; E[eV] ≈ 1239,84 / λ[nm].
- **Cuerpo negro:** L = 4π R² σ T⁴; λ_máx = b / T con b = 2,8978 × 10⁻³ m K.
- **Temperatura de equilibrio:** T_eq = [L (1 − A) / (16 π σ d²)]^¼.
- **Eventos:** 1 tonelada de TNT = 4,184 × 10⁹ J.
- **Potencia:** 1 L☉ = 3,828 × 10²⁶ W.
- **Escala de Kardashev (Sagan):** K = (log₁₀ P − 6) / 10, con P en W. Humanidad ≈ 0,7.
- **Escala sísmica:** log₁₀ E ≈ 1,5 M_w + 4,8 (E en J, orden de magnitud).

📘 [B05](../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md "Física fundamental para el espacio"), [B31](../programa/tronco-comun/B31-fisica-cuantica-nuclear-y-astroparticulas.md "Física cuántica, nuclear y astropartículas"), [B85](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md "Gestión térmica y entorno espacial").

---

## 7. Escalas de clima espacial, riesgo y madurez

- **Clases de llamaradas solares (GOES, rayos X de 0,1–0,8 nm):** A < 10⁻⁷, B 10⁻⁷, C 10⁻⁶, M 10⁻⁵, X 10⁻⁴ W/m²; "M5.2" = 5,2 × 10⁻⁵ W/m². Cada letra es 10 veces la anterior.
- **Escalas de la NOAA:** G (tormentas geomagnéticas, 1–5), S (radiación solar, 1–5) y R (apagones de radio, 1–5).
- **Índice Kp:** 0 a 9 de actividad geomagnética.
- **Escala de Turín (0–10):** riesgo de impacto de un asteroide, y **escala de Palermo** (logarítmica, relativa al riesgo de fondo).
- **TRL (1–9):** madurez tecnológica.

📘 [B33](../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md "Clima espacial: impactos, pronóstico y riesgo"), [B34](../programa/tronco-comun/B34-corona-solar-y-erupciones-diagnostico-y-modelos.md "Corona solar y erupciones: diagnóstico y modelos"), [B58](../programa/tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md "Asteroides, cometas y defensa planetaria"), [B83](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md "Ingeniería de sistemas y diseño de misiones").

---

## 8. Fórmulas para recordar (con unidades)

| Fórmula | Qué da | Unidades | Supuesto |
|---|---|---|---|
| T = 2π √(a³ / GM) | Periodo orbital | s (a en m, GM en m³ s⁻²) | Dos cuerpos |
| v = √(GM (2/r − 1/a)) | Velocidad en cualquier punto (vis-viva) | m/s | Dos cuerpos |
| v_c = √(GM / r) | Velocidad circular | m/s | Órbita circular |
| v_e = √(2 GM / r) | Velocidad de escape | m/s | Sin atmósfera |
| Δv₁ = √(GM/r₁) (√(2r₂/(r₁+r₂)) − 1) | Primer impulso de Hohmann | m/s | Circulares coplanares |
| Δv = Isp g₀ ln(m₀ / m_f) | Ecuación del cohete | m/s | Sin pérdidas |
| r_s = 2GM / c² | Radio de Schwarzschild | m | Agujero negro sin rotación |
| θ ≈ 1,22 λ / D | Límite de difracción | rad | Apertura circular |
| Escala de placa = 206 265 / f [mm] | Segundos de arco por mm | arcsec/mm | Aproximación de ángulos pequeños |
| 1 + z = λ_obs / λ_emit | Corrimiento al rojo | adimensional | — |
| v/c = ((1+z)² − 1) / ((1+z)² + 1) | Velocidad radial relativista | adimensional | Efecto Doppler |
| r_H ≈ a (1 − e) (m / 3M)^⅓ | Esfera de Hill | m | Tres cuerpos restringido |

Cada una está implementada en la calculadora; mira la función con el mismo nombre en el código y el caso de `autotest`. 📘 [B71](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental"), [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B41](../programa/tronco-comun/B41-optica-geometrica-y-diseno-de-telescopios.md "Óptica geométrica y diseño de telescopios"), [B26](../programa/tronco-comun/B26-relatividad-y-cosmologia.md "Relatividad y cosmología").

---

## 9. Ejemplos resueltos

**Ejemplo 1 · ¿Cuánto tarda la luz del Sol?** t = 1 UA / c = 149 597 870 700 / 299 792 458 ≈ **499,0 s** (8 min 19 s). Comprobación: `calc "UA/c"`.

**Ejemplo 2 · Periodo de la ISS.** a = 6378,1 km + 400 km = 6778,1 km; T = 2π √(a³/GM) ≈ **92,6 min**. Comprobación: `orbita --a 6778100`.

**Ejemplo 3 · Distancia por módulo.** Una estrella con m = 5 y M = 0: d = 10^((5 − 0 + 5)/5) pc = **100 pc**. Comprobación: `modulo-distancia --m 5 --M 0`.

**Ejemplo 4 · Δv de una transferencia LEO → GEO.** De r₁ = 6678 km a r₂ = 42 164 km: Δv total ≈ **3,89 km/s** (impulsos instantáneos, coplanar). Comprobación: `hohmann --r1 6678e3 --r2 42164e3`. Una transferencia real incluye cambio de plano, pérdidas y margen.

**Ejemplo 5 · Cohete.** Isp = 450 s, m₀ = 1000 kg, m_f = 300 kg: Δv ≈ **5,31 km/s**. Comprobación: `cohete --isp 450 --m0 1000 --mf 300`.

---

## 10. Cómo verificar tus cálculos

1. **Anota los datos y las unidades** (con la fuente y versión).
2. **Haz el cálculo a mano** y con la calculadora; compara con una tolerancia que justifiques.
3. **Revisa el orden de magnitud** (¿velocidades orbitales de ~ 7–8 km/s? ¿luminosidad solar ~ 10²⁶ W?).
4. **Cambia un dato y observa** cuánto cambia el resultado (sensibilidad).
5. **Documenta supuestos:** modelo, marco de referencia, escala de tiempo.

[⬅️ Anexo H](ANEXO-H-cronologia.md) · [Índice de anexos](README.md) · [Siguiente: Anexo J · Estudios de caso →](ANEXO-J-estudios-de-caso-a-fondo.md)
