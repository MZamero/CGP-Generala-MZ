# Jugada: representa los 5 dados
# valor: el valor del dado que estoy buscando en mi jugada
# retorno: cantidad de veces que aparece
# apraiciones_por_dado representa la contidad de repeticiones por cada dado


def esServida(intentos):
    return intentos == 1


def alNumero(cubil, valor):
    repeticiones = 0
    for dad in cubil:
        if dad == int(valor):
            repeticiones += 1
    return repeticiones


def esEscalera(cubil):
    cubil.sort()
    return ((cubil == [1, 2, 3, 4, 5]) or
            (cubil == [2, 3, 4, 5, 6]))


def esFull(cubil):
    cubil.sort()
    return ((cubil[0] == cubil[1] == cubil[2] and cubil[2] != cubil[3] == cubil[4]) or
            (cubil[0] == cubil[1] != cubil[2] and cubil[2] == cubil[3] == cubil[4]))


def esPoker(cubil):
    cubil.sort()
    return ((cubil[0] == cubil[1] == cubil[2] == cubil[3] != cubil[4]) or
            (cubil[0] != cubil[1] == cubil[2] == cubil[3] == cubil[4]))


def esGenerala(cubil):
    return cubil[0] == cubil[1] == cubil[2] == cubil[3] == cubil[4]


def esDobleGenerala(cubil, generala):
    return (cubil[0] == cubil[1] == cubil[2] == cubil[3] == cubil[4]) and generala==50


def determinarGeneralaServida(cubil, intentos):
    return (cubil[0] == cubil[1] == cubil[2] == cubil[3] == cubil[4]) and intentos == 1


def tablacategorias(cubil, gene):
    funCat = {"1": alNumero(cubil, 1),
              "2": alNumero(cubil, 2),
              "3": alNumero(cubil, 3),
              "4": alNumero(cubil, 4),
              "5": alNumero(cubil, 5),
              "6": alNumero(cubil, 6),
              "Escalera": esEscalera(cubil),
              "Full": esFull(cubil),
              "Poker": esPoker(cubil),
              "Generala": esGenerala(cubil),
              "Doble generala": esDobleGenerala(cubil, gene)
              }
    return funCat

# CATEGORIAS(? FINAL
