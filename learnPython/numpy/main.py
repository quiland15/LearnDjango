import numpy as np

vectorA = np.array([1,2,3,4])

print(f"Vector A = {vectorA}")

matrixA = np.array([(1,2),(3,4)])

print(f"Matrix A = \n{matrixA}")

zerosA = np.zeros((2,2))
print(f"Zeros A = \n{zerosA}")

onesA = np.ones((2,2))
print(f"Ones A = \n{onesA}")

jumlah = matrixA + matrixA**2 + onesA
print(jumlah)