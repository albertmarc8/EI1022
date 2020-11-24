from utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed


def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self, mochila, pendiente, v):  # IMPLEMENTAR: Añade los parámetros que tú consideres
            self.mochila = mochila # equivalente a "decisiones"
            self.pendiente = pendiente
            self.n = len(mochila)
            self.v = v

        def is_solution(self) -> bool:  # IMPLEMENTAR
            return self.mochila == len(weights)

        def get_solution(self) -> Solution:  # IMPLEMENTAR
            return self.mochila

        def successors(self) -> Iterable["KnapsackPS"]:  # IMPLEMENTAR
            if self.n < len(weights):
                yield KnapsackPS(self.mochila + (0,), self.pendiente)
                if weights[self.n] <= self.pendiente:
                    yield KnapsackPS(self.mochila + (1,), self.pendiente - weights[self.n], self.v * values[self.n])

        def state(self) -> State:  # IMPLEMENTAR
            return self.pendiente, self.n

        def f(self) -> Union[int, float]:  # IMPLEMENTAR
            return -sum(self.mochila[i] * values[i] for i in range(len(self.mochila)))
            #return -self.v
            #return -sum(m * values[i] for i, m in enumerate(self.mochila))

    initialPS = KnapsackPS((), capacity, 0)  # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)


def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int, ...], Tuple[int, ...], int]:
    seed(42)
    weights = [int(random() * 1000 + 1) for _ in range(num_objects)]
    values = [int(random() * 1000 + 1) for _ in range(num_objects)]
    capacity = sum(weights) // 2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
    W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7  # SOLUCIÓN: Weight=7,    Value=9
    # W, V, C = create_knapsack_problem(30)     # SOLUCIÓN: Weight=6313, Value=11824
    for sol in knapsack_solve(W, V, C):
        w = sum(W[i] * m for i, m in enumerate(sol))
        v = sum(V[i] * m for i, m in enumerate(sol))

        print(f"Weight : {w}, Value = {v}: {sol}")
    print("\n<TERMINADO>")
