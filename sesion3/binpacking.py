from typing import *
from random import random, seed

def mientras_quepa(objetos: List[int], capacidad: int) -> List[int]:
    contenedores = []
    contador_contenedor, capacidad_almacenada = 0, 0
    for objeto in objetos:
        if (capacidad_almacenada+objeto) > capacidad:
            capacidad_almacenada = 0
            contador_contenedor += 1
        capacidad_almacenada += objeto
        contenedores.append(contador_contenedor)
    print(contenedores)
    return contenedores


def primero_que_quepa(objetos: List[int], capacidad: int) -> List[int]:
    libres = []
    contenedores = []
    for objeto in objetos:
        pos = -1
        for i in range(len(libres)):
            if libres[i] > objeto:
                pos = i
                break
        if pos == -1:
            libres.append(capacidad)
            pos = len(libres) - 1
        contenedores.append(pos)
        libres[pos] -= objeto
    return contenedores


def primero_que_quepa_ordenado(objetos: List[int], capacidad: int) -> List[int]:
    libres = []
    contenedores = [0] * len(objetos)
    indices_ordenados = sorted(range(len(objetos)), key = lambda i: -objetos[i])

    for i in range(len(objetos)):
        pos = -1
        for j in range(len(libres)):
            if libres[j] > objetos[j]:
                pos = j
                break
        if pos == -1:
            libres.append(capacidad)
            pos = len(libres) - 1
        contenedores[i] = pos
        libres[pos] -= objetos[i]
    return contenedores


def prueba_binpacking():
    W, C = [1, 2, 8, 7, 8, 3], 10
    # seed(42)
    # W, C = [int(random()*1000)+1 for i in range(1000)], 1000

    for solve in [mientras_quepa, primero_que_quepa, primero_que_quepa_ordenado]:
        print("-" * 40)
        print("Método:", solve.__name__)
        try:
            sol = solve(W, C)
            print("Usados {} contenedores: {}".format(1 + max(sol), sol))
        except NotImplementedError:
            print("No implementado")


if __name__ == "__main__":
    prueba_binpacking()