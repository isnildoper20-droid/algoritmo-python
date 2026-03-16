# Algoritmo A* , Heurística y Teoría de Juegos en Python

## Autor
Isnildo Equia  
Estudiante de Ingeniería de Sistemas

---

## Descripción del Proyecto

Este proyecto presenta la implementación del **Algoritmo A*** (A estrella) utilizando Python para encontrar el camino más corto entre dos puntos en una cuadrícula.

Además, se incluyen ejemplos de:

- Heurísticas utilizadas en inteligencia artificial
- Aplicaciones básicas de la teoría de juegos

El objetivo del proyecto es demostrar cómo los algoritmos de búsqueda informada pueden optimizar procesos de decisión y encontrar soluciones eficientes a problemas complejos.

---

## Objetivos

### Objetivo General

Implementar el algoritmo de búsqueda A* en Python y demostrar su funcionamiento junto con ejemplos de heurísticas y teoría de juegos.

### Objetivos Específicos

- Comprender el funcionamiento del algoritmo A*
- Implementar heurísticas para optimizar la búsqueda
- Analizar ejemplos básicos de teoría de juegos
- Desarrollar simulaciones simples utilizando Python

---

## Algoritmo A*

El algoritmo **A*** es un algoritmo de búsqueda informada ampliamente utilizado en inteligencia artificial para encontrar el camino más corto entre dos nodos.

Este algoritmo utiliza la función:

f(n) = g(n) + h(n)

donde:

- **g(n)** representa el costo desde el nodo inicial hasta el nodo actual
- **h(n)** representa una estimación heurística del costo desde el nodo actual hasta el objetivo
- **f(n)** representa el costo total estimado

El algoritmo A* se utiliza en:

- Videojuegos
- Sistemas GPS
- Robótica
- Planificación de rutas
- Inteligencia artificial

---

## Heurística

Una **heurística** es un método utilizado para estimar la mejor solución de un problema de forma rápida.

En el algoritmo A*, la heurística ayuda a estimar la distancia entre el nodo actual y el objetivo.

### Ejemplos de heurísticas

1. **Distancia Manhattan**

Se utiliza en movimientos de cuadrícula (arriba, abajo, izquierda, derecha).

h(n) = |x1 - x2| + |y1 - y2|

2. **Distancia Euclidiana**

Se utiliza cuando el movimiento puede realizarse en cualquier dirección.

h(n) = √((x1-x2)² + (y1-y2)²)

---

## Teoría de Juegos

La **Teoría de Juegos** es una rama de las matemáticas que estudia la toma de decisiones estratégicas entre varios jugadores.

Analiza situaciones donde el resultado depende de las decisiones de todos los participantes.

### Aplicaciones

- Economía
- Inteligencia artificial
- Estrategia militar
- Política
- Negociación
- Juegos

### Ejemplos implementados en el proyecto

1. Dilema del prisionero  
2. Piedra, papel o tijera  
3. Estrategias simples de decisión

---

## Estructura del Proyecto
