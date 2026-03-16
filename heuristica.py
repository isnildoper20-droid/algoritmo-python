import math

def distancia_manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def distancia_euclidiana(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def ejemplo_heuristica():

    puntoA = (2,3)
    puntoB = (5,7)

    print("Distancia Manhattan:")
    print(distancia_manhattan(puntoA,puntoB))

    print("Distancia Euclidiana:")
    print(distancia_euclidiana(puntoA,puntoB))