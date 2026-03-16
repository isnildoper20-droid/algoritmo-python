import heapq

# 🔹 Heurística (Manhattan)
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 🔹 Vecinos
def vecinos(nodo, grid):
    x, y = nodo
    posibles = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    resultado = []

    for nx, ny in posibles:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] != 1:
                resultado.append((nx, ny))
    return resultado

# 🔹 A*
def a_estrella(grid, inicio, objetivo):
    abiertos = []
    heapq.heappush(abiertos, (0, inicio))

    camino = {}
    g = {inicio: 0}

    while abiertos:
        _, actual = heapq.heappop(abiertos)

        if actual == objetivo:
            return camino

        for vecino in vecinos(actual, grid):
            nuevo_g = g[actual] + 1

            if vecino not in g or nuevo_g < g[vecino]:
                g[vecino] = nuevo_g
                f = nuevo_g + heuristica(vecino, objetivo)

                heapq.heappush(abiertos, (f, vecino))
                camino[vecino] = actual

    return camino

# 🔹 Dibujar árbol del recorrido
def dibujar_arbol(camino, inicio, objetivo):
    print("\n🌳 Árbol de recorrido:\n")

    for hijo, padre in camino.items():
        print(f"{padre}  →  {hijo}")

    print("\n📍 Ruta final:\n")

    # reconstruir ruta
    actual = objetivo
    ruta = [actual]

    while actual in camino:
        actual = camino[actual]
        ruta.append(actual)

    ruta.reverse()

    # dibujar tipo árbol
    for i, nodo in enumerate(ruta):
        if i == 0:
            print(f"{nodo} (Inicio)")
        elif i == len(ruta)-1:
            print("   " * i + f"└── {nodo} (Meta)")
        else:
            print("   " * i + f"└── {nodo}")

# 🔹 GRID
grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

inicio = (0,0)
objetivo = (2,2)

# 🔹 Ejecutar
camino = a_estrella(grid, inicio, objetivo)

dibujar_arbol(camino, inicio, objetivo)
