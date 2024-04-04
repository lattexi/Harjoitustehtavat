import numpy as np

# Kertoimien matriisi A
A = np.array([[1, 4, 2],
              [4, -3, 0],
              [2, 2, 2]])

# Vakiotermit B
B = np.array([10, 6, 14])

# Lasketaan käänteismatriisi A_inv
A_inv = np.linalg.inv(A)

# Ratkaistaan yhtälöryhmä
X = np.dot(A_inv, B)

print("Ratkaisu X on:", X)
