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


def phrase(matrix1, matrix2, operation):
    
    return f"{operation(matrix1, matrix2)}"


def get_matrix(choice):
    matrices = {"1": A, "2": B, "3": t_a, "4": t_b}
    return matrices.get(choice, None)



def menu():
    print("1. Add matrices")
    print("2. Multiply matrices")
    choice = input("Enter your choice: ")
    if choice in ["1", "2"]:
        operation = add_matrices if choice == "1" else multiply_matrices
        print("Select first matrix:")
        print("1. A\n2. B\n3. C\n4. A transpose\n5. B transpose\n6. C transpose")
        matrix1 = get_matrix(input("Enter your choice: "))
        print("Select second matrix:")
        print("1. A\n2. B\n3. C\n4. A transpose\n5. B transpose\n6. C transpose")
        matrix2 = get_matrix(input("Enter your choice: "))
        if matrix1 is not None and matrix2 is not None:
            print(phrase(matrix1, matrix2, operation))
        else:
            print("Invalid matrix selection.")


menu()
