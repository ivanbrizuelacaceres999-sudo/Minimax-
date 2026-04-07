#  Conceptos Técnicos del Proyecto: Gato vs Ratón IA

Este proyecto implementa un sistema de toma de decisiones automatizado utilizando técnicas clásicas de Inteligencia Artificial y programación estructurada en Python.

---

### 🧠 1. Inteligencia Artificial y Algoritmos
* **Algoritmo Minimax:** Motor principal de decisión para juegos de suma cero. Explora todas las jugadas posibles para elegir la mejor opción.
* **Recursividad Mutua:** La función se llama a sí misma alternando estados para simular los turnos del oponente.
* **Caso Base:** Condición de parada para la recursividad (cuando la profundidad llega a 0 o hay una captura).
* **Heurística (Función de Evaluación):** Estimación numérica de qué tan "buena" es una posición en el tablero basándose en distancias.
* **Horizonte de Predicción:** Límite de pasos hacia el futuro que la IA analiza (Profundidad).


### 📐 3. Matemáticas y Geometría
* **Distancia Manhattan:** Cálculo de distancia en rejillas rectangulares mediante la suma de diferencias absolutas: `abs(x1-x2) + abs(y1-y2)`.
* **Lógica de Desempate:** Criterio secundario para elegir movimientos cuando el futuro parece tener el mismo valor.
* **Maximización vs Minimización:** El Ratón busca el valor máximo (alejarse) y el Gato el mínimo (acercarse).

### 🐍 4. Programación Avanzada en Python
* **Matrices (Nested Lists):** Representación bidimensional del mundo virtual.
* **List Comprehension:** Filtrado eficiente de movimientos válidos en una sola línea de código.
* **Desempaquetado de Tuplas:** Manejo limpio de coordenadas `(x, y)`.
* **Variables Dummy (`_`):** Estándar para ignorar datos de retorno innecesarios en la recursión.
* **Operador Ternario:** Asignación condicional de la profundidad para optimizar el flujo.

---
*Proyecto desarrollado para el aprendizaje de estructuras de datos y algoritmos de búsqueda.*
