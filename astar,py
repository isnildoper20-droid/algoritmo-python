import heapq

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_estrella(grid, inicio, objetivo):

    filas = len(grid)
    columnas = len(grid[0])

    movimientos = [(0,1),(1,0),(0,-1),(-1,0)]

    open_list = []
    heapq.heappush(open_list,(0,inicio))

    costo = {inicio:0}
    camino = {}

    while open_list:

        _,actual = heapq.heappop(open_list)

        if actual == objetivo:
            break

        for mov in movimientos:

            vecino = (actual[0]+mov[0], actual[1]+mov[1])

            if 0 <= vecino[0] < filas and 0 <= vecino[1] < columnas:

                if grid[vecino[0]][vecino[1]] == 1:
                    continue

                nuevo_costo = costo[actual] + 1

                if vecino not in costo or nuevo_costo < costo[vecino]:

                    costo[vecino] = nuevo_costo

                    prioridad = nuevo_costo + heuristica(objetivo,vecino)

                    heapq.heappush(open_list,(prioridad,vecino))

                    camino[vecino] = actual

    ruta = []
    nodo = objetivo

    while nodo != inicio:
        ruta.append(nodo)
        nodo = camino[nodo]

    ruta.append(inicio)
    ruta.reverse()

    return ruta