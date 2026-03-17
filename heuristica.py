import networkx as nx
import matplotlib.pyplot as plt

# =========================
#  Coordenadas de nodos
# =========================
coordenadas = {
    'A': (0,0),
    'B': (1,1),
    'C': (2,1),
    'D': (3,2),
    'F': (4,2)  # objetivo
}

# =========================
#  Grafo
# =========================
grafo = {
    'A': ['B','C'],
    'B': ['C','D'],
    'C': ['D'],
    'D': ['F'],
    'F': []
}

# =========================
#  Función heurística
# =========================
def heuristica(nodo, objetivo):
    x1, y1 = coordenadas[nodo]
    x2, y2 = coordenadas[objetivo]
    return abs(x1 - x2) + abs(y1 - y2)

# =========================
#  Calcular heurísticas
# =========================
objetivo = 'F'
valores_h = {}

print("🔎 CÁLCULO DE HEURÍSTICA:\n")

for nodo in coordenadas:
    h = heuristica(nodo, objetivo)
    valores_h[nodo] = h

    x1, y1 = coordenadas[nodo]
    x2, y2 = coordenadas[objetivo]

    print(f"{nodo}: |{x1}-{x2}| + |{y1}-{y2}| = {h}")

# =========================
#  Dibujar grafo
# =========================
def dibujar_grafo(grafo, heuristica_vals):
    Gnx = nx.DiGraph()

    for nodo in grafo:
        for vecino in grafo[nodo]:
            Gnx.add_edge(nodo, vecino)

    pos = nx.spring_layout(Gnx)

    etiquetas = {}
    for nodo in grafo:
        etiquetas[nodo] = f"{nodo}\nh={heuristica_vals[nodo]}"

    plt.figure()
    nx.draw(Gnx, pos, labels=etiquetas, with_labels=True)
    plt.title("Grafo con valores heurísticos")
    plt.show()

dibujar_grafo(grafo, valores_h)
