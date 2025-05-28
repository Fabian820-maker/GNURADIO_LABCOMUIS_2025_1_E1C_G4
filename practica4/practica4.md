# Práctica 4: Monitoreo del Espectro Radioeléctrico y Señales Moduladas en Ángulo

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
La práctica 4 consta de dos partes: la primera consistió en el monitoreo del espectro radioeléctrico entre 88 y 108 MHz para estudiar las emisoras con cobertura en el laboratorio, y la segunda en el análisis de señales moduladas en ángulo de banda ancha y estrecha.

**Parte A:** Se utilizó una antena del laboratorio y GNU Radio para sintonizar y analizar las frecuencias de emisoras de radio FM. Con el analizador de espectros y GNU Radio se identificaron características de las señales, como el piloto, L+R, y se comprendió cómo la Agencia Nacional del Espectro (ANE) define el ancho de banda de estas emisoras.

**Parte B:** Se exploraron modulaciones de banda estrecha y banda ancha usando GNU Radio y osciloscopio, variando el índice de modulación (KpAm) para observar los cambios en el tiempo. Además, se calcularon los coeficientes de Bessel teóricos con ayuda de tablas proporcionadas, para entender mejor la naturaleza de estas modulaciones.

---

## Estructura de Carpetas
- **parteA:** Contiene los archivos de configuración (.grc y .py) y las evidencias correspondientes al monitoreo del espectro radioeléctrico.
- **parteB:** Incluye los archivos relacionados con la modulación en ángulo y las evidencias sobre las modulaciones de banda estrecha y ancha, además de los cálculos realizados.

---

## Procedimiento

### Parte A: Monitoreo del Espectro Radioeléctrico
1. Se conectó la antena del laboratorio al sistema GNU Radio para sintonizar el rango de frecuencias entre 88 y 108 MHz.
2. Se identificaron y analizaron las diferentes emisoras presentes en el espectro mediante el analizador de espectros y GNU Radio.
3. Se observaron características de las señales como el tono piloto y la señal L+R.
4. Se revisó la regulación del ancho de banda por la Agencia Nacional del Espectro (ANE).

### Parte B: Señales Moduladas en Ángulo (FM y PM)
1. Se configuró GNU Radio para generar señales moduladas en banda estrecha y ancha variando el índice de modulación (KpAm).
2. Se observaron las señales en el dominio temporal con el osciloscopio, notando diferencias en comportamiento y forma según el ancho de banda.
3. Se calcularon teóricamente los coeficientes de Bessel con tablas proporcionadas para comparar con las señales observadas.
4. Se analizaron los resultados para comprender el efecto del índice de modulación en las señales en ángulo.

---

## Resultados y Análisis

- En el monitoreo del espectro se pudo identificar claramente las emisoras y sus características, entendiendo la estructura de sus señales.
- La banda asignada por ANE limita el ancho de banda de las emisoras, aspecto crucial para evitar interferencias.
- Las señales moduladas en ángulo mostraron comportamientos distintos al variar el índice de modulación, evidenciado en la forma de la señal en el osciloscopio.
- Los coeficientes de Bessel calculados teóricamente ayudaron a entender la distribución de potencia en las componentes espectrales de las señales moduladas.

---

## Conclusiones

- La experiencia de monitoreo real permitió comprender el funcionamiento y regulación del espectro radioeléctrico en FM.
- GNU Radio es una herramienta potente para la generación y análisis de señales moduladas en ángulo, facilitando la visualización de efectos de banda ancha y estrecha.
- El cálculo de coeficientes de Bessel complementa el análisis experimental, ofreciendo un fundamento teórico sólido.
- Esta práctica refuerza conceptos de comunicaciones analógicas y la importancia del espectro en la transmisión eficiente.

---

### Referencias
- [Proakis, 2014] J. Proakis, M. Salehi. Fundamentals of Communication Systems. 2 ed. Pearson Education Limited, 2014.
- Documentación de GNU Radio: https://www.gnuradio.org/
- Manual del Analizador de Espectros R&S FPC1000
- Manual del Osciloscopio R&S RTB2004
- Regulación ANE: Agencia Nacional del Espectro

---
