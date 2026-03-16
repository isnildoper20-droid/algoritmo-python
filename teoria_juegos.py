import random

def dilema_prisionero(j1, j2):

    if j1 == "traicionar" and j2 == "traicionar":
        return "Ambos reciben castigo medio"

    elif j1 == "traicionar" and j2 == "cooperar":
        return "Jugador 1 libre, Jugador 2 castigo alto"

    elif j1 == "cooperar" and j2 == "traicionar":
        return "Jugador 2 libre, Jugador 1 castigo alto"

    else:
        return "Ambos reciben castigo bajo"


def piedra_papel_tijera():

    opciones = ["piedra","papel","tijera"]

    jugador = random.choice(opciones)
    computadora = random.choice(opciones)

    print("Jugador:",jugador)
    print("Computadora:",computadora)

    if jugador == computadora:
        print("Empate")

    elif (jugador=="piedra" and computadora=="tijera") or \
         (jugador=="papel" and computadora=="piedra") or \
         (jugador=="tijera" and computadora=="papel"):

        print("Jugador gana")

    else:
        print("Computadora gana")