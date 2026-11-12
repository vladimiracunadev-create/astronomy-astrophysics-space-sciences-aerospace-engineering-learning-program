# Capítulo 3 · Lanzador, masas y vehículo

## Por qué existe este capítulo

La nave pesaba unas **3 toneladas** y la mayor parte era **combustible**: iba a frenar para quedar con un cometa. Eso, más una sonda y unos paneles solares enormes, definió un vehículo grande y delicado.

## El lanzador

- **Ariane 5 (versión G+)** de la ESA y Arianespace, desde Kourou (Guayana Francesa), el **2 de marzo de 2004**.
- Con un viaje de asistencias gravitatorias, el cohete **no necesitaba** la potencia de una trayectoria directa.

## La nave

| Parte | Datos de referencia (⚠ redondeados) |
|---|---|
| Masa total al lanzamiento | ≈ 3.000 kg |
| Combustible (propelente) | ≈ 1.700 kg (más de la mitad) |
| Sonda Philae | ≈ 100 kg |
| Paneles solares | ≈ 64 m² en total, ≈ 32 m de punta a punta |
| Antena principal | ≈ 2,2 m de diámetro |
| Instrumentos del orbitador | 11 |
| Instrumentos de la sonda | 10 |

## La ecuación del cohete en acción

Más de la mitad de la nave era combustible: la mayor parte para **frenar** al llegar al cometa y para las maniobras de mantenimiento durante dos años. El laboratorio común (`masa_propelente`) permite calcular cuánto hace falta para un cambio de velocidad dado: con Isp ≈ 320 s, 1,5 km/s sobre una nave de 1.300 kg seca exige unos 1.700 kg.

## Masa y reservas

El diseño equilibró tres cosas que compiten:

- **Paneles grandes** para producir energía lejos del Sol.
- **Combustible** para frenar y mantener la órbita.
- **Una sonda** con instrumentos propios, de masa mínima.

Cada kilogramo que se añade a la sonda reduce el combustible disponible. La **tabla CBE / reserva / MEV** (T01) controló el balance.

## La sonda Philae

Un módulo de **≈ 100 kg** con 10 instrumentos, un **tren de aterrizaje** con arpones y tornillos de hielo para anclarse, y un propulsor de gas frío para apretarse contra el suelo. Funcionaría con una **batería primaria** de ≈ 60 horas y luego con paneles solares si había suficiente luz (⚠ verifica).

## Herencia

Los instrumentos de la nave heredaron diseños de misiones anteriores de la ESA, y la plataforma tenía un **diseño modular** reutilizable (otras misiones europeas lo usaron). Una misión de diez años exige **componentes de alta fiabilidad**, con vida útil certificada.

## Ejercicio del capítulo

1. Calcula el propelente necesario para frenar 1,2 km/s con Isp 320 s sobre una nave de 1.500 kg seca.
2. Elabora la tabla de masas de una nave similar, con CBE, reserva y MEV, y decide qué reserva darías a la sonda.
3. Explica por qué los paneles de 64 m² son necesarios y cómo se compara su masa con la de un generador nuclear de potencia equivalente.

Anterior: [capítulo 2](02-ventana-y-trayectoria.md) · Siguiente: [capítulo 4](04-subsistemas.md)
