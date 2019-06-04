import random
dados = [0, 0, 0, 0, 0]

def tiro(*args):
    if not args:
        args = [0, 1, 2, 3, 4]
    for i in args:
        dados[i] = random.randrange(1, 7)
    return dados


def jugada():
    cubilete = tiro()
    print(cubilete)
    intentos = 1
    while intentos < 3:
        d = input("Ingrese posición del dado a cambiar (separado por un punto / 0 para terminar): ")
        if d == "0":
            print(dados)
            return dados, intentos
        else:
            f = d.split(".")
            for t in f:
                tiro(int(t) - 1)
            print(dados)
            intentos += 1
    return dados, intentos
# CUBILETE FINAL
