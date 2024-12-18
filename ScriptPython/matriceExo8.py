import numpy as np


M = np.matrix("0 1 0 0; 0 0 0 1; 1 0 0 0; 0 0 1 0")

# Verifier que det(M) = -1
det_M = round(np.linalg.det(M))
print("det(M) = -1", det_M == -1)

