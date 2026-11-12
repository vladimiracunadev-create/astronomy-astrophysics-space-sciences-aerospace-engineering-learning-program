# Capítulo 1 · Objetivo y requisitos

## Por qué existe este capítulo

Demo-2 es un **vuelo de certificación**: su propósito no es la ciencia sino **demostrar que el sistema es seguro** para llevar tripulaciones de forma rutinaria. Eso cambia cómo se escriben los requisitos: cada uno es una prueba que debe pasarse.

## El contexto

Tras el retiro del transbordador en 2011, Estados Unidos dependió de cohetes rusos para llevar astronautas a la estación. La NASA creó el **Programa de Tripulación Comercial**: en vez de comprar y operar una nave, **compra un servicio** a empresas, que desarrollan y operan el vehículo bajo requisitos de seguridad de la agencia. Demo-2 fue el último gran examen antes de la certificación.

## Objetivos (con palabras propias)

1. **Demostrar el vuelo completo** con personas: lanzamiento, vuelo autónomo, acoplamiento, estancia y regreso.
2. **Validar** el soporte vital, los trajes, la interfaz de la tripulación y los sistemas en condiciones reales.
3. **Verificar** los procedimientos de operación y de emergencia con el control de misión.
4. **Obtener la certificación** para misiones de tripulación regulares.

## Requisitos que mandan

| Requisito | Origen | Consecuencia de diseño |
|---|---|---|
| Probabilidad de pérdida de la tripulación (LOC) ≤ 1 en 270 por misión a la estación (⚠ verifica el valor vigente) | Requisito de la agencia | Redundancia, sistema de aborto, análisis de riesgo continuo |
| Abortar en cualquier punto del ascenso | Seguridad de la tripulación | Motores de aborto integrados en la cápsula |
| Acoplarse de forma autónoma, con supervisión manual | Seguridad de la estación | Sensores relativos y modo manual de respaldo |
| Volver con seguridad ante fallos | Seguridad | Cápsula independiente con soporte vital propio |

## La restricción que manda: no se puede perder a nadie

En una misión robótica, un fallo **cuesta dinero**; en una tripulada, **cuesta vidas**. Eso eleva las exigencias de redundancia, de pruebas y de **cultura de seguridad**: se prefiere **no volar** a volar con una duda sin resolver.

## Niveles de éxito

- **Mínimo:** los dos tripulantes vuelven sanos.
- **Completo:** además, se valida la certificación sin condiciones.
- **Extendido:** las misiones siguientes llevan tripulaciones completas de cuatro personas.

## Ejercicio del capítulo

1. Redacta **diez requisitos** de un vuelo de certificación y la **prueba** que verifica cada uno.
2. Explica con tus palabras la diferencia entre **comprar una nave** y **comprar un servicio**: riesgos, responsabilidades y costo.
3. Define qué **evidencia** exigirías para declarar «seguro» un vehículo antes de llevar personas.

Siguiente: [capítulo 2 · Ventana y trayectoria](02-ventana-y-trayectoria.md) · [índice](README.md)
