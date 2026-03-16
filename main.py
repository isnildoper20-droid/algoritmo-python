from astar import a_estrella
from heuristica import ejemplo_heuristica
from teoria_juegos import dilema_prisionero, piedra_papel_tijera

grid = [
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],
[0,1,0,0]
]

inicio = (0,0)
objetivo = (3,3)

ruta = a_estrella(grid,inicio,objetivo)

print("Ruta encontrada con A*")
print(ruta)

print("\nEjemplo de heuristica")
ejemplo_heuristica()

print("\nTeoria de juegos")
print(dilema_prisionero("cooperar","traicionar"))

print("\nJuego Piedra Papel Tijera")
piedra_papel_tijera()