from typing import *

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


def path(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Vertex]:
    def go(u: Vertex, v: Vertex):
        seen.add(v)
        edges.append((u, v))
        for suc in g.succs(v):
            if suc not in seen:
                go(v, suc)

    edges = []
    seen = set()
    go(source, source)
    return recover_path(edges, target)


def shortest_path(grafo: UndirectedGraph, source: Vertex, target: Vertex) -> List[Edge]:
    # sys.setrecursionlimit(10000) # en el caso de que el laberinto sea más grande, por lo tanto, la recursión más larga
    edges = []
    queue = Fifo()
    seen = set()
    queue.push((source, source))
    seen.add(source)
    while len(queue) > 0:
        u, v = queue.pop()
        edges.append((u, v))
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return recover_path(edges, target)


def recover_path(edges: List[Edge], target: Vertex):
    bp = {}
    for u, v in edges:
        bp[v] = u
    v = target
    path = [v]
    while bp[v] != v:
        v = bp[v]
        path.append(v)
    path.reverse()
    return path
