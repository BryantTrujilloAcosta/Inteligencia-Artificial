# INTELIGENCIA ARTIFICIAL 9-10

## TAREA 5
# Resolver Puzzle 8

Este proyecto resuelve el rompecabezas Puzzle 8 utilizando búsqueda en anchura (BFS).



El programa generará un tablero aleatorio y tratará de resolverlo. Si es resoluble, mostrará los pasos hasta llegar a la solución.

## Estructura del Código
- `Tablero`: Maneja el estado del puzzle, los movimientos posibles y verifica si es resoluble.
- `ResolverPuzzle`: Implementa el algoritmo BFS para encontrar la solución.

## Ejemplo de Salida
```
Tablero inicial:
(1, 2, 3)
(4, 5, 6)
(7, 0, 8)

Moviendo vacío de (2, 1) a (2, 2):
(1, 2, 3)
(4, 5, 6)
(7, 8, 0)

Tablero resuelto:
(1, 2, 3)
(4, 5, 6)
(7, 8, 0)
```

Si el estado inicial no es resoluble, el programa lo indicará.


