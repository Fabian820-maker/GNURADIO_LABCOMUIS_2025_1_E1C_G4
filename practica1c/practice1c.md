# Práctica 1: Mediciones de potencia y frecuencia

### Integrantes
- **Jaiver Josept Buitrago Graterón** - 2204277
- **[Nombre del Segundo Integrante]** - [Código]

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

### Fecha
[Fecha de realización del laboratorio]

---

## Declaración de Originalidad y Responsabilidad
Los autores de este informe certifican que el contenido aquí presentado es original y ha sido elaborado de manera independiente. Se han utilizado fuentes externas únicamente como referencia y han sido debidamente citadas.

Asimismo, los autores asumen plena responsabilidad por la información contenida en este documento.

Uso de IA: Se utilizó ChatGPT para estructurar el informe y mejorar la redacción, pero el contenido técnico y los análisis fueron desarrollados íntegramente por los autores.

---

## Contenido

### Resumen
En esta práctica, se emplearon herramientas de medición como el USRP 2920, el osciloscopio R&S RTB2004 y el analizador de espectros R&S FPC1000, junto con el software de simulación GNU Radio, para realizar mediciones y análisis de parámetros clave en comunicaciones, incluyendo potencia, ancho de banda, relación señal a ruido (SNR) y piso de ruido. Además, se analizó el comportamiento de una señal modulada en frecuencia, observando los cambios al variar los parámetros tanto del mensaje como de la portadora.

**Palabras clave:** GNU Radio, USRP 2920, osciloscopio, analizador de espectros, SNR, piso de ruido.

### Introducción
...

### Procedimiento
**Actividad 1: Revisión de Especificaciones de los Equipos**

1. **Revisión de Manuales y Verificación de Equipos:**
   - Se consultaron las especificaciones técnicas del USRP 2920, el osciloscopio R&S RTB2004 y el analizador de espectros R&S FPC1000 para comprender sus capacidades y limitaciones.
   - Verificamos la correcta conexión y funcionamiento de cada equipo antes de iniciar las mediciones.

2. **Configuración de Equipos para Mediciones:**
   - Configuramos el USRP 2920 para generar señales en frecuencias específicas y con niveles de potencia controlados.
   - Ajustamos el osciloscopio para visualizar las señales en el dominio del tiempo y frecuencia, asegurando una correcta sincronización y escala.
   - Utilizamos el analizador de espectros para medir el espectro de las señales generadas, identificando componentes de frecuencia y niveles de potencia.

**Actividad 2: Mediciones de Señales con el Osciloscopio**

1. **Generación de Señales con GNU Radio y USRP 2920:**
   - A partir del diagrama de flujo en GNU Radio para generar una señal sinusoidal de 1 kHz con una amplitud de 1 Vpp entregado por el docente se transmitió la señal utilizando el USRP 2920.

2. **Visualización y Análisis de la Señal en el Osciloscopio:**
   - Conectamos la salida del USRP 2920 al osciloscopio y observamos la forma de onda de la señal.
   - Medimos parámetros como frecuencia, amplitud y ciclo útil, comparándolos con los valores esperados.

**Actividad 3: Análisis en el Dominio de la Frecuencia con el Analizador de Espectros**

1. **Medición del Espectro de la Señal Generada:**
   - Conectamos la salida del USRP 2920 al analizador de espectros.
   - Observamos el espectro de la señal, identificando la frecuencia fundamental y posibles armónicos.

2. **Cálculo de la Relación Señal a Ruido (SNR):**
   - Medimos la potencia de la señal fundamental y del ruido de fondo.
   - Calculamos la SNR utilizando la fórmula: \( \text{SNR} = 10 \log_{10} \left( \frac{P_{\text{señal}}}{P_{\text{ruido}}} \right) \).

**Actividad 4: Evaluación del Piso de Ruido del Sistema**

1. **Medición del Piso de Ruido:**
   - Con el USRP 2920 inactivo, medimos el nivel de ruido presente en el sistema utilizando el analizador de espectros.
   - Identificamos las fuentes de ruido y evaluamos su impacto en las mediciones.

### Conclusiones
- La familiarización con las especificaciones y configuración de equipos como el USRP 2920, el osciloscopio R&S RTB2004 y el analizador de espectros R&S FPC1000 es crucial para realizar mediciones precisas en sistemas de comunicación.
- El uso de herramientas como GNU Radio en conjunto con hardware SDR permite la generación y análisis flexible de señales, facilitando la experimentación y comprensión de conceptos clave en comunicaciones.
- La correcta medición y análisis de parámetros como potencia, ancho de banda, SNR y piso de ruido son fundamentales para el diseño y evaluación de sistemas de comunicación eficientes.

### Referencias
- [Proakis, 2014] J. Proakis, M. Salehi. Fundamentals of communication systems. 2 ed. England: Pearson Education Limited, 2014. p. 164-165, 346. Chapter 5 In: [Biblioteca UIS](https://uis.primo.exlibrisgroup.com/permalink/57UIDS_INST/63p0of/cdi_askewsholts_vlebooks_9781292015699)
- [Manual del USRP 2920](https://www.ni.com/pdf/manuals/375715a.pdf)
- [Guía de usuario del osciloscopio R&S RTB2004](https://www.rohde-schwarz.com/manual/rtb2000)
- [Manual del analizador de espectros R&S FPC1000](https:// 