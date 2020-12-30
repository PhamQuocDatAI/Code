# Viết 1 hàm tạo ra 1 ma trận số nguyên có định thức bằng 1.
import numpy as np
import random
a = int(input("Số cột:"))
A = np.zeros( (a, a), dtype = np.int)
for x in range(a):
    for y in range(a):
        A[x][y] = random.randint(-5, 5)
# Làm sao để có det = 1 ???
while np.linalg.det(A) != 1:
    for x in range(a):
        for y in range(a):
            A[x][y] = random.randint(-5, 5)
print(A)
print(np.linalg.det(A))

