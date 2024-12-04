import numpy as np

A = np.matrix("2 1 2; 1 1 3; 2 2 1")
B = np.matrix('1 0 1; 2 1 1; 0 1 1')


def transpose(matrix):
    return np.transpose(matrix)


t_a = transpose(A)
t_b = transpose(B)


def add_matrices(matrix1, matrix2):
    try:
        return np.add(matrix1, matrix2)
    except ValueError:
        return "Matrices must have the same dimensions"


def multiply_matrices(matrix1, matrix2):
    try:
        return np.dot(matrix1, matrix2)
    except ValueError:
        return "The number of columns of the first matrix must be equal to the number of rows of the second matrix"


def determinant(matrix):
    return np.linalg.det(matrix)

# Calculer C = A x B et D = B x A, les matricent A et B commutent-elles ?
C = multiply_matrices(A, B)
D = multiply_matrices(B, A)
if np.array_equal(C, D):
    print("Les matrices A et B commutent")
else:
    print("Les matrices A et B ne commutent pas")

# Calculer les déterminants det(A), det(B), det(C) et det(D)
det_A = determinant(A)
det_B = determinant(B)
det_C = determinant(C)
det_D = determinant(D)
# Vérifier que det(C) = det(D) = det(A) x det(B)
if det_C == det_D == det_A * det_B:
    print("det(C) = det(D) = det(A) x det(B)")
else:
    print("det(C) != det(D) != det(A) x det(B)")
# Pourquoi les matrices A,B,C,D sont-elles inversibles ?
# Les matrices sont inversibles car leur déterminant est différent de 0
print("A est inversible : ", det_A != 0)
print("B est inversible : ", det_B != 0)
print("C est inversible : ", det_C != 0)
print("D est inversible : ", det_D != 0)
# Inverser les matrices A et B par la méthode de Gauss, puis par la méthode des comatrices
A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)
print("A_inv : \n", A_inv)
print("B_inv : \n", B_inv)
# Vérifier que C_inv = B_inv x A_inv et D_inv = A_inv x B_inv
C_inv = np.linalg.inv(C)
D_inv = np.linalg.inv(D)
if np.array_equal(C_inv, np.dot(B_inv, A_inv)) and np.array_equal(D_inv, np.dot(A_inv, B_inv)):
    print("C_inv = B_inv x A_inv et D_inv = A_inv x B_inv")
else:
    print("C_inv != B_inv x A_inv ou D_inv != A_inv x B_inv")