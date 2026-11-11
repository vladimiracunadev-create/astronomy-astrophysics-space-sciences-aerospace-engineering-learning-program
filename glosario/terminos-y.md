# Términos · Y

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · **Y** · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

### Y

- En astronomía, X es la fracción en masa del hidrógeno, Y la del helio y Z la de todo lo demás, llamado en bloque «metales» aunque incluya carbono, nitrógeno y oxígeno (S1).

🎯 **Por qué importa (clase B06-C02):** Cuando alguien dice «el universo es casi todo hidrógeno y helio», ¿en qué sentido es cierto? ¿En número de átomos, en masa, en el Sol, en la Tierra?

📘 **Dónde se aprende** (1 clase): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md).

### YAML

- JSON es un formato de texto para intercambiar datos entre lenguajes; sus valores son objeto, arreglo, número, texto, `true`, `false` y `null` (S2, S3). YAML es un formato legible por personas para serializar datos con tres estructuras: mapeos (clave-valor), secuencias (listas) y escalares (valores simples); la estructura se marca con sangría y no admite tabulaciones en ella (S4).

💡 **Cómo se explica en la clase [B07-C16](../programa/clases/B07/B07-C16-formatos-json-y-yaml/CLASE.md):**
- Nunca uses tabulaciones para sangrar: YAML no las admite (S4);
- La versión 1.2 de YAML es un superconjunto de JSON (todo JSON válido es YAML válido), según la especificación (S4).
- ⚠️ **Error frecuente:** Usar `yaml.load` con datos ajenos. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Una simulación tiene decenas de parámetros. Si están enterrados en el código, cambiar uno obliga a editar el programa y es fácil olvidar con qué valores se obtuvo cada resultado.

📘 **Dónde se aprende** (1 clase): [B07-C16 · Formatos JSON y YAML](../programa/clases/B07/B07-C16-formatos-json-y-yaml/CLASE.md).

### Yoon–Nelson

- Ruptura: momento en que el lecho deja pasar el contaminante. Yoon–Nelson: modelo de la curva de ruptura.

💡 **Cómo se explica en la clase [B106-C21](../programa/clases/B106/B106-C21-depuracion-de-trazas-gaseosas-de-la-atmosfera-de-cabina/CLASE.md):**
- Usar el modelo de Yoon–Nelson para el tiempo al 10 % y 90 % de ruptura.
- El script [depuracion_de_trazas.py](depuracion_de_trazas.py) calcula el estacionario, la vida de un lecho (con Yoon–Nelson), la conversión de un catalizador frente a la temperatura y el tren combinado (comprueba el estacionario contra la integración y el 0,5 de la ruptura en `τ`).
- 🎯 **Por qué importa:** Una cabina cerrada acumula trazas que no son CO₂ ni agua; hay que retirarlas con lechos y catalizadores que se saturan o dependen de la temperatura. La decisión central: ¿cuánto dura un lecho, a qué temperatura debe operar el catalizador y qué concentración queda en la cabina?

📘 **Dónde se aprende** (1 clase): [B106-C21 · Depuración de trazas gaseosas de la atmósfera de cabina](../programa/clases/B106/B106-C21-depuracion-de-trazas-gaseosas-de-la-atmosfera-de-cabina/CLASE.md).

### YORP

- El efecto Yarkovsky es el empuje por la reemisión térmica anisótropa de un cuerpo que rota. YORP es el torque análogo que cambia la rotación.

💡 **Cómo se explica en la clase [B58-C14](../programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/CLASE.md):**
- La evidencia es la ficha de Yarkovsky y YORP del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de Yarkovsky y YORP*: comparación integrada–fórmula, tabla física y barrera.
- 🎯 **Por qué importa:** Una deriva de decenas de kilómetros en un siglo puede decidir si un acercamiento ocurre. La decisión central: ¿cuánto se desplaza un asteroide por empuje térmico y por qué los cuerpos pequeños son más sensibles?

📘 **Dónde se aprende** (1 clase): [B58-C14 · Efectos Yarkovsky y YORP](../programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/CLASE.md).
