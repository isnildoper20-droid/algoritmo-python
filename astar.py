import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

#  Grafo manual (no matriz)
G = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

#  Heurística (para A*)
heuristica = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}

# ======================
#  BFS (Anchura)
# ======================
def bfs(grafo, inicio, objetivo):
    cola = deque([[inicio]])
    visitados = set()

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == objetivo:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in grafo[nodo]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None

# ======================
#  DFS (Profundidad)
# ======================
def dfs(grafo, inicio, objetivo, camino=None, visitados=None):
    if camino is None:
        camino = [inicio]
    if visitados is None:
        visitados = set()

    if inicio == objetivo:
        return camino

    visitados.add(inicio)

    for vecino in grafo[inicio]:
        if vecino not in visitados:
            resultado = dfs(grafo, vecino, objetivo, camino + [vecino], visitados)
            if resultado:
                return resultado

    return None

# ======================
#  A*
# ======================
def a_estrella(grafo, inicio, objetivo):
    abiertos = []
    heapq.heappush(abiertos, (0, inicio))

    camino = {}
    g = {inicio: 0}

    while abiertos:
        _, actual = heapq.heappop(abiertos)

        if actual == objetivo:
            return reconstruir(camino, actual)

        for vecino in grafo[actual]:
            nuevo_g = g[actual] + 1

            if vecino not in g or nuevo_g < g[vecino]:
                g[vecino] = nuevo_g
                f = nuevo_g + heuristica[vecino]

                heapq.heappush(abiertos, (f, vecino))
                camino[vecino] = actual

    return None

def reconstruir(camino, actual):
    ruta = [actual]
    while actual in camino:
        actual = camino[actual]
        ruta.append(actual)
    ruta.reverse()
    return ruta

# ======================
#  Dibujar grafo
# ======================
def dibujar_grafo(grafo, ruta, titulo):
    Gnx = nx.DiGraph()

    for nodo in grafo:
        for vecino in grafo[nodo]:
            Gnx.add_edge(nodo, vecino)

    pos = nx.spring_layout(Gnx)

    plt.figure()

    nx.draw(Gnx, pos, with_labels=True)

    if ruta:
        edges = [(ruta[i], ruta[i+1]) for i in range(len(ruta)-1)]
        nx.draw_networkx_edges(Gnx, pos, edgelist=edges, width=3)

    plt.title(titulo)
    plt.show()

# ======================
# EJECUCIÓN
# ======================
inicio = 'A'
objetivo = 'F'

ruta_bfs = bfs(G, inicio, objetivo)
ruta_dfs = dfs(G, inicio, objetivo)
ruta_astar = a_estrella(G, inicio, objetivo)

print("BFS (Anchura):", ruta_bfs)
print("DFS (Profundidad):", ruta_dfs)
print("A*:", ruta_astar)

dibujar_grafo(G, ruta_bfs, "BFS (Anchura)")
dibujar_grafo(G, ruta_dfs, "DFS (Profundidad)")
dibujar_grafo(G, ruta_astar, "A* (Heurístico)")
