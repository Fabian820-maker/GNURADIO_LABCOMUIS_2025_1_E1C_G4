# Práctica 5: Modulaciones Digitales y de Pulsos

### Integrantes
- **Jaiver Josept Buitrago Graterón** - 2204277
- **Nelson Fabian Valbuena Carreño** - 2181556

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

---

## Declaración de Originalidad y Responsabilidad
Los autores certifican que el contenido de este informe es original y elaborado de forma independiente. Se usó ChatGPT solo para mejorar redacción y estructura, pero todo el contenido técnico es propio.

---

## Contenido

### Resumen 

Esta práctica se enfoca en dos grandes temas dentro de las modulaciones digitales y de pulsos:

- **Parte A:** Modulación por amplitud de pulsos (PAM), incluyendo el análisis en dominios de tiempo y frecuencia, multiplexación y demodulación.
- **Parte B:** Técnicas de cuantización digital, comparando la cuantización uniforme y la Ley U, evaluando su impacto en la calidad de la señal y ruido.

---

## Parte A: Modulación PAM

### Objetivo

Analizar la modulación por amplitud de pulsos (PAM) en los dominios del tiempo y frecuencia, y entender el proceso de multiplexación y demodulación de señales PAM.

### Desarrollo

1. Se estudiaron los conceptos básicos de modulación PAM, PWM y PPM, destacando su aplicación en transmisión digital.
2. Se configuró un bloque jerárquico en GNU Radio llamado "MODULADOR DE PULSOS", donde se definieron parámetros como frecuencia de pulsos (`fs`), frecuencia de muestreo (`samp_rate`) y ancho de pulso (`D`).
3. Se analizaron diferentes formas de onda moduladas PAM con relación `samp_rate/fs = 100`.
4. Se multiplexaron cuatro y cinco señales PAM usando retardos (`Delay`) para evitar superposición, calculando los retardos como porcentaje del ciclo útil.
5. Se demodularon las señales sumadas, conectando el USRP para mediciones y ajustando filtros pasabajas para recuperar cada canal.

### Resultados

- Se observaron claramente las señales PAM moduladas en tiempo y frecuencia.
- La multiplexación fue exitosa sin interferencia entre señales.
- La demodulación permitió recuperar cada señal individualmente, validado con osciloscopio y analizador de espectros.

---

## Parte B: Cuantización Uniforme y Ley U

### Objetivo

Explorar técnicas de cuantización en procesamiento digital, comparando la cuantización uniforme y la Ley U para mejorar la calidad de la señal y reducir el ruido.

### Desarrollo

1. Se implementó un cuantizador uniforme en GNU Radio, observando el efecto del número de bits en el ruido de cuantización.
2. Se analizaron preguntas sobre la resolución, el ruido gaussiano, y el impacto del ancho de banda del filtro pasabajas.
3. Se implementó la cuantización Ley U, ajustando la constante U para estudiar su efecto en la distribución de niveles y ruido.
4. Se compararon ambos métodos en osciloscopio y analizador de espectro, evaluando calidad y relación señal-ruido.

### Resultados

- La cuantización uniforme mostró un aumento del ruido con baja resolución.
- La Ley U mejoró la resolución en amplitudes bajas sin aumentar el número de bits.
- Se validó la optimización de parámetros para mejorar la relación señal-ruido.
- Observaciones en osciloscopio y analizador de espectro confirmaron los análisis teóricos.

---

## Conclusiones

- La modulación PAM permite transmitir señales digitales con éxito, y la multiplexación facilita el envío simultáneo de múltiples señales sin interferencia.
- La cuantización es crucial en el procesamiento digital, y la Ley U es una técnica eficiente para mejorar calidad sin aumentar la complejidad.
- Las herramientas GNU Radio, USRP, osciloscopio y analizador de espectro son fundamentales para la experimentación y validación práctica.

---

## Referencias

- [Proakis, 2014] J. Proakis, M. Salehi. Fundamentals of Communication Systems. 2 ed. Pearson Education Limited, 2014.
- Documentación de GNU Radio: https://www.gnuradio.org/
- Manual del Analizador de Espectros R&S FPC1000
- Manual del Osciloscopio R&S RTB2004
- Notas de clase de Comunicaciones

---