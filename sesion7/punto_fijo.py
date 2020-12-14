from typing import *

def punto_fijo(v: List[int]) -> Optional[int]:
    def punto_fijo_parcial(i: int, j: int) -> Optional[int]:
        if i == j:
            return None

        m = (i + j) // 2
        if v[m] == m:
            return m
        if v[m] > m:
            return punto_fijo_parcial(i, m)
        return punto_fijo_parcial(m + 1, j)

    return punto_fijo_parcial(0, len(v))

if __name__ == "__main__":
    print(punto_fijo([-10,-5,1,3,6]))
    print(punto_fijo([-10,-5,1,2,6]))
    print(punto_fijo([0, 2, 3, 5, 6]))
    print(punto_fijo([-10, 1, 2, 3, 4]))