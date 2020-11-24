from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
import random


def create_labyrinth(rows, cols, n=0):
    # Crea una lista, vertices, con los vértices del grafo (nuestras celdas del laberinto).
    vertices = []
    for row in range(rows):
        for col in range(cols):
            vertices.append((row, col))
    # vertices = [(r,c) for r in range(rows) for c in range(cols)] <-- versión del profesor

    # Crea un MFSet vacío, mfs, y añádele uno a uno los vértices de la lista vertices usando su método add.
    # Para crear un MFSet utiliza la clase MergeFindSet disponible en algoritmia.datastructures.mergefindsets.
    mfs = MergeFindSet()
    for vertice in vertices:
        mfs.add(vertice)

    # Crea una lista, edges, con todos los pares de vértices vecinos y barájala. Usa la función
    # shuffle del módulo random.
    edges = []
    for row in range(rows):
        for col in range(cols):
            if col > 0:
                edges.append(((row, col), (row, col - 1)))
            if row > 0:
                edges.append(((row, col), (row - 1, col)))

    # edges = [((row, col), (row, col + 1)) for r in range(rows) for c in range(cols-1)]
    # edges.extend(
    #     [((row, col), (row, col + 1)) for r in range(rows-1) for c in range(cols)]
    # )
    random.shuffle(edges)

    # Crea una lista vacía, corridors. Aquí pondremos las aristas (pasillos) que tendrá al final
    # nuestro grafo (laberinto).
    corridors = []

    # Recorre la lista edges y, para cada arista (u,v), encuentra la clase a la que pertenece
    # cada uno de los dos vértices usando find. Si son diferentes, fusiónalas en la misma clase con
    # merge y añade la arista (u,v) a la lista corridors.
    for u, v in edges:
        if mfs.find(u) != mfs.find(v):
            corridors.append((u, v))
            mfs.merge(u, v)
        else:
            if n > 0:
                corridors.append((u, v))
                #mfs.merge(u, v)
                n -= 1

    # El laberinto es el grafo no dirigido que tiene a la lista corridors como conjunto de aristas:
    # return UndirectedGraph(E = corridors)
    # print("Corridors: ")
    # print(corridors)
    return UndirectedGraph(E=corridors)
