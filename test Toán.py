import numpy as np
import random
# Viết hàm cho ra một ma trận số nguyên cấp n ngẫu nhiên.
def matrix(n):
    matrix = np.random.randint(-10, 10, size = (n, n))
    detmatrix = np.linalg.det(matrix)
    rankmatrix = np.linalg.matrix_rank(matrix)
    return matrix, detmatrix, rankmatrix

n = int(input("Nhập giá trị n: "))
a , b, c = matrix(n)
print("Ma trận cấp ", n," là: ", a)
print("Định thức của ma trận cấp ", n," là: ", b)
print("Rank của ma trận cấp ", n," là: ", b)
# Viết hàm tính định thức của 1  ma trận số nguyên cấp n ngẫu nhiên.
def detmatrix(n):
    detmatrix = np.linalg.det(matrix(n))
    return int(detmatrix)

print("Định thức của ma trận cấp ", n," là: ", detmatrix(n))
# Viết hàm tính hạng của ma trận 
def rankmatrix(n):
    rankmatrix = np.linalg.matrix_rank(matrix(n))
    return rankmatrix

print("Rank của ma trận cấp ", n," là: ", rankmatrix(n))
# Viết hàm tính lũy thừa bậc 2, 3 của ma trận
def luy_thua_matrix(n):
    x = int(input("Nhập giá trị x: "))
    while x < 0:
        x = int(input("Nhập giá trị x: "))
    while x > 0:
        luy_thua_matrix = matrix(n) @ matrix(n)
    return luy_thua_matrix

print(luy_thua_matrix(n))