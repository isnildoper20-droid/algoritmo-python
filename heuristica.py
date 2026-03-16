import math

# Heurística Manhattan
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Función de búsqueda simple usando heurística
def busqueda_heuristica(grid, inicio, objetivo):

    actual = inicio
    camino = [actual]

    while actual != objetivo:

        x, y = actual

        vecinos = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]

        vecinos_validos = []

        for v in vecinos:

            if 0 <= v[0] < len(grid) and 0 <= v[1] < len(grid[0]):

                if grid[v[0]][v[1]] != 1:
                    vecinos_validos.append(v)

        mejor = min(vecinos_validos, key=lambda v: heuristica(v, objetivo))

        camino.append(mejor)

        actual = mejor

    return camino


# MAPA (0 = libre, 1 = obstáculo)
grid = [
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],
[0,1,0,0]
]

inicio = (0,0)
objetivo = (3,3)

camino = busqueda_heuristica(grid, inicio, objetivo)

print("Recorrido del camino:")
for paso in camino:
    print(paso)

# Mostrar mapa con recorrido
for x,y in camino:
    grid[x][y] = "*"

print("\nMapa con el recorrido:")

for fila in grid:
    print(fila)