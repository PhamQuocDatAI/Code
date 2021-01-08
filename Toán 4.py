import numpy as np
import random
import sympy 
def matrix(m, n):
    matrix = np.random.randint(-10, 10, size = (m, n))
    rank_matrix = np.linalg.matrix_rank(matrix)
    return matrix, rank_matrix

m = random.randint(-5, 5) 
n = random.randint(-5, 5)
while ((m < 2) or (n < 2)):
    m = random.randint(-5, 5) 
    n = random.randint(-5, 5)

a, b = matrix(m, n)
print(a)
print(b)


def bac_thang(m, n):
    bac_thang = bac_thang.rref()
    return bac_thang

print(bac_thang(m, n))





# Nếu random cột hàng của matrix -> Lưu ý số hàng, số cột != 0