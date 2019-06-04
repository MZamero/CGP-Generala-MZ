from tabulate import tabulate
import categorias as cat

def servida(intentos):
    if intentos is True:
        return 5
    return 0


def puntNormal(repeticiones, valor):
    uno_a_seis = int(repeticiones) * int(valor)
    return uno_a_seis


def puntEscalera(esCalera, intentos):
    if esCalera is True:
        return 20+intentos
    return 0


def puntFull(esFull, intentos):
    if esFull is True:
        return 30+intentos
    return 0


def puntPoker(esPoker, intentos):
    if esPoker is True:
        return 40+intentos
    return 0


def puntGenerala(esGenerala):
    if esGenerala is True:
        return 50
    return 0


def puntDobleGenerala(esDobleGenerala):
    if esDobleGenerala is True:
        return 60
    return 0


def generalaServida(generala, intentos, lista, turno):
    if generala is True and intentos == 1:
        return "El ganador es "+ lista[turno]

def tablaFunciones(repeticiones, intentos):
    funPun = {"1": puntNormal(repeticiones, 1),
              "2": puntNormal(repeticiones, 2),
              "3": puntNormal(repeticiones, 3),
              "4": puntNormal(repeticiones, 4),
              "5": puntNormal(repeticiones, 5),
              "6": puntNormal(repeticiones, 6),
              "Escalera": puntEscalera(repeticiones, servida(intentos)),
              "Full": puntFull(repeticiones, servida(intentos)),
              "Poker": puntPoker(repeticiones, servida(intentos)),
              "Generala": puntGenerala(repeticiones),
              "Doble generala": puntDobleGenerala(repeticiones)
              }
    return funPun
