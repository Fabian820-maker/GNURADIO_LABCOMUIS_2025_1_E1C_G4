# Práctica 3: Modulaciones Lineales - Modulación AM

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
En esta práctica se estudió la modulación de amplitud (AM) como una técnica de modulación lineal. Se diseñó y analizó un sistema en GNU Radio para modular señales con distintos índices de modulación (ka), evaluando su potencia y envolvente en el dominio del tiempo. La Parte B amplió el análisis comparando señales moduladas con diferentes valores de ka usando el analizador de espectros y el osciloscopio, para observar cómo afecta el índice de modulación las características de la portadora y la señal modulada.

**Palabras clave:** Modulación AM, GNU Radio, índice de modulación, potencia de señal, análisis en dominio del tiempo y frecuencia.

---

## Estructura de Carpetas
- **DatosyFotos:** Contiene los datos experimentales y fotografías tomadas durante la práctica.
- **parteA:** Archivos .grc y .py correspondientes a la Parte A del experimento, donde se diseña y analiza el sistema de modulación AM.
- **parteB:** Archivos .grc y .py de la Parte B, que extiende el análisis comparando configuraciones con distintos índices de modulación.

---

## Procedimiento

### Parte A: Diseño y Análisis de Modulación AM en GNU Radio
1. Se diseñó un modelo en GNU Radio para modular una señal de prueba con diferentes índices de modulación (ka).
2. Se ejecutaron simulaciones para observar la señal modulada en el dominio del tiempo y frecuencia.
3. Se midió la potencia de la señal modulada para cada valor de ka.
4. Se analizó la envolvente de la señal para verificar la modulación en amplitud.

### Parte B: Comparación y Medición con Equipos de Laboratorio
1. Se implementaron las configuraciones de modulación con distintos índices de modulación (ka) usando GNU Radio.
2. Se conectó el sistema al analizador de espectros y al osciloscopio para medir las señales generadas.
3. Se analizaron los cambios en la portadora y en la señal completa al variar el índice de modulación.
4. Se registraron observaciones sobre cómo la potencia y la forma de la envolvente cambian con ka.

---

## Resultados y Análisis

- Se observó que el aumento del índice de modulación (ka) incrementa la variación de amplitud en la señal modulada, lo que se refleja en la envolvente de la señal.
- La potencia de la señal modulada se comporta de manera proporcional al índice de modulación, confirmando la teoría de modulación AM.
- El analizador de espectros mostró un espectro con bandas laterales características de la modulación AM, cuya amplitud varía con ka.
- El osciloscopio permitió visualizar la envolvente de la señal, facilitando la comparación directa entre diferentes valores de ka.

---

## Conclusiones

- La modulación AM puede ser fácilmente simulada y analizada usando GNU Radio, permitiendo un control directo sobre el índice de modulación.
- La potencia y la forma de la señal modulada dependen directamente del índice de modulación, afectando la calidad y eficiencia de la transmisión.
- El análisis combinado con osciloscopio y analizador de espectros es fundamental para entender el comportamiento completo de señales moduladas en AM.
- Esta práctica refuerza los conceptos teóricos vistos en clase y muestra la importancia de las herramientas de medición en la evaluación de sistemas de comunicación.

---

### Referencias
- [Proakis, 2014] J. Proakis, M. Salehi. Fundamentals of Communication Systems. 2 ed. Pearson Education Limited, 2014.
- Documentación de GNU Radio: https://www.gnuradio.org/
- Manual del Analizador de Espectros R&S FPC1000
- Manual del Osciloscopio R&S RTB2004

---

