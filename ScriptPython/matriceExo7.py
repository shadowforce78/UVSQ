# Soit les matrices :
import numpy as np

M = np.matrix("0 1 0; 2 0 0; -2 0 1")
M1 = np.matrix("2 0 0; 0 1 0; -2 0 1")
M2 = np.matrix("1 0 0; 0 1 0; -2 0 1")
I3 = np.matrix("1 0 0; 0 1 0; 0 0 1")
# Calculer P1, P2, P3
# P1 * M = M1
# P2 * M1 = M2
# P3 * M2 = I3
P1 = np.linalg.inv(M) * M1
P2 = np.linalg.inv(M1) * M2
P3 = np.linalg.inv(M2) * I3
print("P1 = \n", P1)
print("P2 = \n", P2)
print("P3 = \n", P3)

# Justifier M^-1 = P1 * P2 * P3 * I3
M_inv = np.linalg.inv(M)
print("M^-1 = \n", M_inv)
print("M^-1 = \n", P1 * P2 * P3 * I3)
