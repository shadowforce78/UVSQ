import numpy as np
from fractions import Fraction

A = np.array(
    [
        [2, 1, 2],
        [1, 1, 3],
        [2, 2, 1],
    ]
)

B = np.array([6, 6, 7])

try:
    A_inv = np.array(
        [[Fraction(x).limit_denominator() for x in row] for row in np.linalg.inv(A)]
    )

    solution = np.linalg.solve(A, B)

    print(f"Matrice inverse de A :\n{A_inv}")
    print("Solution du système :")
    print(f"x = {solution[0]:.2f}, y = {solution[1]:.2f}, z = {solution[2]:.2f}")
except np.linalg.LinAlgError as e:
    print("Erreur :", e)
