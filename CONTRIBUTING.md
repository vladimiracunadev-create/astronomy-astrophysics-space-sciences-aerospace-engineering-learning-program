# Contribuir

Gracias por mejorar el **Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial**. Antes de proponer un cambio, lee `AGENTS.md`, el [contrato del repositorio](documentacion/ALCANCE_Y_CONTRATO_DEL_REPOSITORIO.md) y el [estándar pedagógico](documentacion/ESTANDAR_PEDAGOGICO_Y_DE_EVALUACION.md).

## Reglas esenciales

- Tratarlo como un programa único; no renombrar las 24 rutas como programas independientes.
- No borrar, reutilizar ni renumerar IDs existentes.
- Mantener sincronizados `catalogo/clases.jsonl`, `catalogo/clases.json` y `catalogo/clases.csv`.
- No declarar una clase redactada, impartida o verificada sin superar las puertas E1–E5.
- Añadir contenido con fuentes identificables y límites de uso; no copiar documentación protegida completa.
- Declarar unidades, referencias, datos, versiones, tolerancias e incertidumbre en fórmulas o simulaciones.
- Conservar accesibilidad, seguridad, ética y límites profesionales.
- Integrar otros programas mediante metadatos; no modificar sus repositorios.

## Flujo mínimo

1. Ejecuta la línea base:

   ```bash
   python herramientas/validar_catalogo.py
   ```

2. Describe la necesidad, los IDs afectados, las dependencias y la evidencia.
3. Realiza cambios pequeños y aditivos.
4. Actualiza documentación, estado y changelog si cambió una afirmación actual.
5. Regenera `MANIFIESTO_SHA256.txt` con `python herramientas/generar_manifiesto.py`.
6. Ejecuta nuevamente el validador y registra el resultado.

## Propuestas de contenido

Una propuesta de clase o ampliación debe incluir propósito, resultados observables, prerrequisitos, nivel N0–N5, fuentes, actividad, evidencia, evaluación, continuidad y análisis antirrepetición. Los contenidos se resuelven primero como piloto; no se generan miles de plantillas para simular completitud.

## Licencias y derecho de contribución

Al enviar una contribución declaras que puedes aportarla y que no incorpora material incompatible o confidencial. El código propio se aporta bajo Apache-2.0; la expresión educativa original, bajo CC BY-NC-SA 4.0. Un dataset, activo o fragmento externo debe registrar titular, fuente, versión, licencia, cambios y atribución antes de incorporarse.

Consulta la [matriz de licenciamiento](documentacion/LICENSING_MATRIX.md). Si no puedes demostrar el permiso de redistribución, incluye una referencia en vez de copiar el recurso.

## Informes de errores

Incluye ID exacto, archivo, comportamiento esperado, evidencia y alcance. Para una fuente o norma, añade organismo, título, versión, fecha, localizador y jurisdicción aplicable.
