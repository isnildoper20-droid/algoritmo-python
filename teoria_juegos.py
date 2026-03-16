import random

# ------------------------------
# 1. DILEMA DEL PRISIONERO
# ------------------------------

def dilema_prisionero(j1, j2):

    if j1 == "traicionar" and j2 == "traicionar":
        resultado = "Ambos reciben castigo medio"

    elif j1 == "traicionar" and j2 == "cooperar":
        resultado = "Jugador 1 libre, Jugador 2 castigo alto"

    elif j1 == "cooperar" and j2 == "traicionar":
        resultado = "Jugador 2 libre, Jugador 1 castigo alto"

    else:
        resultado = "Ambos reciben castigo bajo"

    print("\n--- Dilema del Prisionero ---")
    print("Jugador 1:", j1)
    print("Jugador 2:", j2)
    print("Resultado:", resultado)


# ------------------------------
# 2. PIEDRA PAPEL TIJERA
# ------------------------------

def piedra_papel_tijera():

    opciones = ["piedra", "papel", "tijera"]

    jugador = random.choice(opciones)
    computadora = random.choice(opciones)

    print("\n--- Piedra Papel Tijera ---")
    print("Jugador:", jugador)
    print("Computadora:", computadora)

    if jugador == computadora:
        print("Resultado: Empate")

    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):

        print("Resultado: Jugador gana")

    else:
        print("Resultado: Computadora gana")


# ------------------------------
# 3. COMPETENCIA DE PRECIOS
# ------------------------------

def competencia_precios(a, b):

    if a == "alto" and b == "alto":
        resultado = "Ambas empresas ganan moderadamente"

    elif a == "bajo" and b == "alto":
        resultado = "Empresa A gana más clientes"

    elif a == "alto" and b == "bajo":
        resultado = "Empresa B gana más clientes"

    else:
        resultado = "Ambas empresas reducen ganancias"

    print("\n--- Competencia de Precios ---")
    print("Empresa A:", a)
    print("Empresa B:", b)
    print("Resultado:", resultado)


# ------------------------------
# EJECUCIÓN DE LOS EJEMPLOS
# ------------------------------

dilema_prisionero("cooperar", "traicionar")

piedra_papel_tijera()

competencia_precios("alto", "bajo")