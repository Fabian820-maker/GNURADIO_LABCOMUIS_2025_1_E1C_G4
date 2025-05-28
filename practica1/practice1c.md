# Práctica 1: Mediciones de Potencia y Frecuencia

### Integrantes
- **Jaiver Josept Buitrago Graterón** - 2204277
- **Nelson Fabian Valbuena Carreño** - 2181556

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

### Fecha
28 de Febrero del 2025

---

## Declaración de Originalidad y Responsabilidad
Los autores de este informe certifican que el contenido aquí presentado es original y ha sido elaborado de manera independiente. Se han utilizado fuentes externas únicamente como referencia y han sido debidamente citadas.

Asimismo, los autores asumen plena responsabilidad por la información contenida en este documento.

Uso de IA: Se utilizó ChatGPT para estructurar el informe y mejorar la redacción, pero el contenido técnico y los análisis fueron desarrollados íntegramente por los autores.

---

## Contenido

### Resumen
En esta práctica, se emplearon herramientas de medición como el USRP 2920, el osciloscopio R&S RTB2004 y el analizador de espectros R&S FPC1000, junto con el software de simulación GNU Radio, para realizar mediciones y análisis de parámetros clave en comunicaciones, incluyendo potencia, ancho de banda, relación señal a ruido (SNR) y piso de ruido. Además, se analizó el comportamiento de una señal modulada en Amplitud, observando los cambios al variar los parámetros tanto del mensaje como de la portadora.

**Palabras clave:** GNU Radio, USRP 2920, osciloscopio, analizador de espectros, SNR, piso de ruido.

**Actividad 2: Mediciones de Señales con el Osciloscopio**

### Procedimiento

#### **Actividad 1: Revisión de Especificaciones de los Equipos**

**Objetivo:** Familiarizarse con las especificaciones técnicas de los equipos de laboratorio y entender cómo configurarlos para realizar mediciones.

1. **Revisión de Manuales y Verificación de Equipos:**
   - Se consultaron las especificaciones técnicas del USRP 2920, el osciloscopio R&S RTB2004 y el analizador de espectros R&S FPC1000 para comprender sus capacidades y limitaciones. A continuación, se presentan cinco especificaciones clave de cada equipo:
     - **USRP 2920:**
       1. Rango de frecuencia: 50 MHz - 2.2 GHz
       2. Ancho de banda instantáneo: hasta 20 MHz
       3. Resolución de ADC/DAC: 14 bits (ADC) / 16 bits (DAC)
       4. Interfaz de comunicación: Gigabit Ethernet
       5. Potencia de transmisión: hasta +17 dBm
     - **Osciloscopio R&S RTB2004:**
       1. Ancho de banda: 70 MHz - 300 MHz (según modelo)
       2. Frecuencia de muestreo: hasta 2.5 GSa/s
       3. Resolución vertical: 10 bits
       4. Profundidad de memoria: hasta 10 Mpts por canal
       5. Pantalla táctil de 10.1” con interfaz intuitiva
     - **Analizador de espectros R&S FPC1000:**
       1. Rango de frecuencia: 5 kHz - 1 GHz (expandible a 3 GHz)
       2. Resolución de frecuencia: 1 Hz
       3. Ancho de banda de resolución (RBW): 1 Hz - 3 MHz
       4. Nivel de ruido promedio (DANL): -150 dBm (con preamplificador)
       5. Pantalla de alta resolución y conectividad remota
   - Se verificó la correcta conexión y funcionamiento de cada equipo antes de iniciar las mediciones.

2. **Diferencias en la medición de señales en el dominio del tiempo y en el dominio de la frecuencia:**
   - En el dominio del tiempo, se visualiza la variación de la señal con respecto al tiempo, lo que permite analizar parámetros como amplitud, periodo y forma de onda.
   - En el dominio de la frecuencia, se observa la distribución espectral de la señal, identificando sus componentes frecuenciales y permitiendo analizar aspectos como el ancho de banda, la presencia de armónicos y el ruido de fondo.

3. **Medición del piso de ruido en el analizador de espectros:**
   - El piso de ruido se mide determinando el nivel de señal más bajo presente en el espectro cuando no hay señales activas.

4. **Efecto de la frecuencia central, SPAN y RBW en la medición del piso de ruido:**
   - **Frecuencia central:** Determina la región del espectro que se está observando. Si se selecciona una frecuencia central con interferencias, el piso de ruido puede verse afectado.
   - **SPAN:** Define el ancho del espectro visualizado. Un SPAN más amplio permite ver más señales, pero puede aumentar el nivel de ruido promedio.
   - **RBW (Resolución de Banda):** Un RBW menor permite detectar señales más débiles y mejorar la precisión de la medición del piso de ruido, pero aumenta el tiempo de análisis. Además, si se aumenta el RBW, el piso de ruido baja en potencia visualmente y viceversa.

1. **Medición del Piso de Ruido:**
   - Con el USRP 2920 inactivo, medimos el nivel de ruido presente en el sistema utilizando el analizador de espectros.
   - Identificamos las fuentes de ruido y evaluamos su impacto en las mediciones.

#### **Actividad 2: Simulación de Señales en GNU Radio**

**Objetivo:** Generar y analizar señales en GNU Radio para entender cómo se comportan diferentes formas de onda en tiempo y frecuencia.

1. **Generación de Señales con GNU Radio y USRP 2920:**
   - Se cargó, probó y configuró el diagrama de flujo entregado por el docente en GNU Radio.
   - Se generaron diferentes señales y se variaron sus parámetros como frecuencia, amplitud y fase tanto en el dominio del tiempo como en el dominio de la frecuencia. Estas variaciones se evidencian en la carpeta `images`, donde cada subcarpeta contiene comparaciones de cada variación.
   - Se observaron los siguientes cambios:
     - Al cambiar la frecuencia, el espectro se desplazaba.
     - Al cambiar la amplitud, se observaba un cambio en la potencia de la señal, aumentando o disminuyendo de forma directamente proporcional.
     - En la fase, no se observaban cambios notables ya que, al ser señales continuas en el tiempo, desfasarlas no era algo fácilmente perceptible.
     - Al agregar ruido a la señal, en el dominio del tiempo se añadían valores aleatorios que distorsionaban la señal, mientras que en el dominio de la frecuencia el piso de ruido aumentaba.
     - Al cambiar la forma de onda, el espectro también cambiaba, agregando o eliminando armónicos dependiendo del caso.

2. **Demostración Matemática de la Diferencia entre Señal Flotante y Compleja:**
   - Se comparó la representación matemática de una señal flotante y una señal compleja, destacando la diferencia fundamental entre ambas:
     - **Señal Flotante:**
       \[ F\{A\sin(wt)\} = \frac{A}{2} \left( \delta(w+f) + \delta(w-f) \right) \]
     - **Señal Compleja:**
       \[ F\{A\sin(wt) + A j \sin(wt)\} = F\{A e^{jwt}\} = A \delta(w-f) \]

---

#### **Actividad 3: Transmisión y Medición de Señales con el USRP 2920**

**Objetivo:** Transmitir señales usando el USRP 2920 y medir parámetros clave como potencia, ancho de banda, piso de ruido y relación señal a ruido (SNR).

1. **Configuración del sistema de transmisión:**
   - Se configuró el diagrama de flujo en GNU Radio para la transmisión mediante el USRP 2920.
   - Se estableció la conexión entre el USRP 2920 y el analizador de espectros R&S FPC1000 a través de un cable coaxial.

2. **Observación de la señal en el analizador de espectros:**
   - Al iniciar la transmisión de una señal senoidal pura, se evidenció la presencia de más de dos impulsos en el espectro.
   - Con la orientación del docente, se comprendió que este comportamiento se debía a la saturación del sistema, causada por las limitaciones del hardware al alcanzar su rango máximo de operación.

3. **Medición de potencia en distintas formas de onda:**
   - Se variaron las formas de onda transmitidas y se midió la potencia de cada una utilizando la herramienta de marcadores del analizador de espectros.
   - Se empleó el método de los 20 dB, realizando los siguientes cálculos:
     - Conversión de los valores a Watts.
     - Multiplicación por 2 debido a la simetría del espectro (excepto la componente en DC).
     - Suma de los resultados obtenidos y conversión final a dBm.
   - Las evidencias de este proceso se encuentran en la carpeta `images`, en la subcarpeta `powers`.

4. **Sintonización y análisis de una señal de radio FM:**
   - Se conectó una antena al analizador de espectros para recibir señales de radiofrecuencia.
   - Se sintonizó la emisora 95.7 FM y se realizaron mediciones de ancho de banda y potencia de la señal recibida.
   - Las mediciones y análisis de la señal de radio se encuentran documentados en la carpeta `images`, en la subcarpeta `radio`.

---

### **Actividad 4: Análisis de Resultados y Conclusiones**

#### **Comparación de Resultados**

1. **Diferencias entre simulaciones y mediciones reales:**  
   - Se observó que las señales simuladas en GNU Radio presentan características ideales, sin ruido ni distorsiones significativas, mientras que en las mediciones reales, el ruido afecta la calidad de la señal.
   - En la transmisión real, se evidenció que factores como la saturación del sistema y las limitaciones del hardware pueden alterar la forma esperada de la señal.

2. **Diferencias entre mediciones con osciloscopio y analizador de espectros:**  
   - El osciloscopio permitió observar las señales en el dominio del tiempo, facilitando el análisis de amplitud, periodo y forma de onda.
   - El analizador de espectros mostró la distribución de frecuencia de las señales, permitiendo evaluar parámetros como el ancho de banda y la presencia de armónicos.

#### **Conclusiones Finales**

1. **Limitaciones de los equipos utilizados:**  
   - Se identificó que los equipos poseen restricciones en términos de ancho de banda y sensibilidad, lo que afecta la precisión de las mediciones.
   - La capacidad de procesamiento del USRP 2920 y la resolución del analizador de espectros fueron factores determinantes en la calidad de los datos obtenidos.

2. **Variación de Parámetros:**  
   - La modificación de parámetros como amplitud, frecuencia y fase produce cambios coherentes en los dominios del tiempo y la frecuencia, confirmando las predicciones teóricas. En particular, se verificó que la potencia observada es proporcional al cuadrado de la amplitud de la señal.

3. **Importancia de la simulación previa con GNU Radio:**  
   - La utilización de GNU Radio permitió predecir con mayor precisión los resultados esperados antes de realizar mediciones con el analizador de espectros, proporcionando una visión más clara sobre el comportamiento de las señales y facilitando la comprensión de los conceptos abordados a lo largo del documento.

Las evidencias de los análisis realizados se encuentran en la carpeta `images`, organizadas según el tipo de medición.

---

### Referencias
- [Proakis, 2014] J. Proakis, M. Salehi. Fundamentals of communication systems. 2 ed. England: Pearson Education Limited, 2014. p. 164-165, 346. Chapter 5 In: [Biblioteca UIS](https://uis.primo.exlibrisgroup.com/permalink/57UIDS_INST/63p0of/cdi_askewsholts_vlebooks_9781292015699)
- [USRP 2920](http://www.testdynamics.co.za/Product/PDF/USRP2920.pdf)
- [Osciloscopio R&S RTB2004](https://distron.es/tienda/osciloscopio-rs-rtb2004/)
- [Analizador de espectros R&S FPC1000](https://distron.es/tienda/analizador-de-espectro-rs-fpc1000/)
