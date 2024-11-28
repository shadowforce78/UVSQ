import numpy as np

A = np.matrix('4 1 -2; 0 1 1; 1 -2 0')
B = np.matrix('2 -1 1; 0 1 0')
C = np.matrix('3 -1; 1 0; 0 2')

def transpose(matrix):
    return np.transpose(matrix)

def add_matrices(matrix1, matrix2):
    try:
        return np.add(matrix1, matrix2)
    except ValueError:
        return 'Matrices must have the same dimensions'

def multiply_matrices(matrix1, matrix2):
    try:
        return np.dot(matrix1, matrix2)
    except ValueError:
        return 'The number of columns of the first matrix must be equal to the number of rows of the second matrix'

def phrase(matrix1, matrix2, operation):
    return f'{matrix1} {operation} {matrix2} = \n{operation(matrix1, matrix2)}'

print(phrase(C, A, multiply_matrices))