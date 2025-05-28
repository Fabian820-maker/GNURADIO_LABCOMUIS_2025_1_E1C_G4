# Práctica 2: Modelo de Canal

### Integrantes
- **Jaiver Josept Buitrago Graterón** - 2204277
- **Nelson Fabian Valbuena Carreño** - 2181556

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

### Fecha
21 de Febrero del 2025

---

## Declaración de Originalidad y Responsabilidad
Los autores de este informe certifican que el contenido aquí presentado es original y ha sido elaborado de manera independiente. Se han utilizado fuentes externas únicamente como referencia y han sido debidamente citadas.

Asimismo, los autores asumen plena responsabilidad por la información contenida en este documento.

Uso de IA: Se utilizó ChatGPT para estructurar el informe y mejorar la redacción, pero el contenido técnico y los análisis fueron desarrollados íntegramente por los autores.

---

## Contenido

### Resumen
Al final

**Palabras clave:** GNU Radio, USRP 2920, osciloscopio, analizador de espectros, SNR, piso de ruido.

---

### Procedimiento

#### **Actividad 1: Actividad de simulación**

**Objetivo:** Familiarizarse con algunos fenómenos de canal en un ambiente simulado.

1. **Verificación de Equipos:**
   - Se verificó la correcta conexión y funcionamiento de cada equipo antes de iniciar las mediciones.
   - Se cargó el flujograma entregado por el docente y se hizo el respectivo ajuste para trabajar.

2. **Efectos de Aplicación de un Filtro:**
   - **FILTRO**
      - Para filtrar correctamente mi señal debo de filtrar primero el armónico fundamental para tener la misma frecuencia luego para la forma voy filtrando los demás armónicos. Si se filtran las frcuencias altas de una señal, es decir quitando la componete DC se pierte la frecuencia original de la señal
   - **RUIDO** 
      - A medida que aumenta el ruido se van perdiendo armónicos (la potencia del ruido va alcanzando la potencia de los armónicos) sin embargo un filtro permite pasar aquellos armónicos necesarios para recuperar la señal y de esta forma se elimína el ruido
   - Nota: La ventaja de tener un buen filtro es que en la señal filtrada se mejora la relación señal a ruido; es decir se tiene una buena calidad en la señal.

---

#### **Actividad 2: Fenómenos de canal en el osciloscopio:**

**Objetivo:** Familiarizarse con los fenómenos de un canal alambrico en el dominio del tiempo.

1. **Variacion en la Frecuencia de la Portadora:**
   - A medida que se umenta la frecuencia en la protadora la señal disminuye su amplitud es decir a mayor frecuencia la atecuanción generada por el canal es mayor carpeta freq

2. **Efecto del Ruido en la Amplitud de la Señal:**
   - Al tener una menor amplitud de la señal, esta es mas propensa al ruido, por lo que su forma de onda se va a ver afectada como se observa en la imagen en la carpeta freq en la frecuencia de los 500 MHz *Comentario el profesor dice que a los 500 MHz es el limite de muestreo del osciloscopio no es por efecto del ruido*

---

Wenasss paaa, ya con eso que me diste, acá te dejo la **Actividad 3** bien armadita en el mismo estilo de las anteriores, con introducción, procedimiento y cierre. Mira cómo quedó:

---

### **Actividad 3: Fenómenos de Canal en el Analizador de Espectro**

**Objetivo:**
Familiarizarse con los fenómenos que se presentan en un canal alámbrico real, específicamente en el dominio de la frecuencia, utilizando el USRP y el analizador de espectros.

**Desarrollo de la Actividad:**

1. **Configuración del entorno de transmisión:**

   * Se utilizó el flujograma `filters_flowgraph.grc` en GNU Radio, el cual permite la transmisión de señales a través del USRP 2920.
   * Fue necesario habilitar o deshabilitar bloques como `Channel Model`, `Throttle`, `UHD: USRP Sink`, `UHD: USRP Source` y `Virtual Sink` según la necesidad del experimento, utilizando las teclas **E** (enable) y **D** (disable).
   * Se estableció la frecuencia de muestreo (`samp_rate`) en la forma $\frac{25 \cdot 10^6}{2^n}$, donde **n** es un número entero mayor a 2. Se verificó que esta frecuencia fuera consistente tanto en la configuración como durante la ejecución del flujo.

2. **Conexión al analizador de espectros:**

   * Se encendió y configuró el analizador R\&S®FPC1000.
   * Se conectó a la salida del USRP usando cables coaxiales de diferentes longitudes.
   * Se ajustaron parámetros como el ancho de banda, el span y la escala para observar adecuadamente la respuesta en frecuencia de la señal recibida.

3. **Observaciones y fenómenos analizados:**

   * **Efecto del ruido:**
     El ruido provoca una expansión del espectro, disminuyendo la nitidez de los picos principales y reduciendo la relación señal a ruido. Si bien las simulaciones muestran este comportamiento de forma idealizada, en la práctica se observaron variaciones en potencia debido a las diferencias de impedancia entre equipos:

     * El osciloscopio R\&S®RTB2000 tiene una impedancia alta (1 MΩ), ideal para formas de onda en el tiempo.
     * El analizador de espectros tiene 50 Ω, óptimo para medir potencia en RF.
       Esto afecta directamente la medida de potencia vista en cada instrumento.

---

#### **Conclusiones Finales**

1. **Efecto del ruido sobre la señal:**

   * El ruido genera un ensanchamiento del espectro y reduce la nitidez de los componentes principales de la señal. A pesar de esto, se puede mitigar parcialmente con el uso de filtros adecuados.

2. **Influencia de la distancia en transmisión por cable y antena:**

   * Con cables más largos se observó mayor atenuación y un pequeño retardo. En transmisión por antenas, el alejamiento entre transmisor y receptor causó una disminución notable de la amplitud, además de que elementos cercanos (como una mano) afectaron la señal. Estos efectos pueden compensarse con antenas direccionales o amplificadores.

---

### Referencias
- [Proakis, 2014] J. Proakis, M. Salehi. Fundamentals of communication systems. 2 ed. England: Pearson Education Limited, 2014. p. 164-165, 346. Chapter 5 In: [Biblioteca UIS](https://uis.primo.exlibrisgroup.com/permalink/57UIDS_INST/63p0of/cdi_askewsholts_vlebooks_9781292015699)
- [USRP 2920](http://www.testdynamics.co.za/Product/PDF/USRP2920.pdf)
- [Osciloscopio R&S RTB2004](https://distron.es/tienda/osciloscopio-rs-rtb2004/)
- [Analizador de espectros R&S FPC1000](https://distron.es/tienda/analizador-de-espectro-rs-fpc1000/)
