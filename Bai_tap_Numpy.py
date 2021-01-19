import numpy as np
import random


print("Tạo ma trận A có: ")
row = int(input("Số hàng: "))
column = int(input("Số cột: "))
A = np.zeros((row, column), dtype = int)
for x in range(row):
    for y in range(column):
        print("Nhập giá trị cho ô [", x + 1,"][", y + 1,"] là: ")
        A[x][y] = int(input())
print(A)
print("-" * 50)
print("Ma trận chuyển vị của", A," là:")
print(np.transpose(A))
print("-" * 50)
print("Tạo ma trận B có: ")
row = int(input("Số hàng: "))
column = int(input("Số cột: "))
B = np.zeros((row, column), dtype = int)
for x in range(row):
    for y in range(column):
        print("Nhập giá trị cho ô [", x + 1,"][", y + 1,"] là: ")
        B[x][y] = int(input())
print(B)
try:
    print(A@B)
    print("Successful")
except:
    print("Lỗi kích thước ở ma trận B. Vui lòng nhập đúng kích thước. ")
    for x in A.shape:
        pass
    print("Ma trận A có kích thước ", A.shape," ma trận B phải có kích thước (", x,"* x )" )
    print("Tạo ma trận B có: ")
    row = int(input("Số hàng: "))
    column = int(input("Số cột: "))
    B = np.zeros((row, column), dtype = int)
    for x in range(row):
        for y in range(column):
            print("Nhập giá trị cho ô [", x + 1,"][", y + 1,"] là: ")
            B[x][y] = int(input())


def matrix(m, n):
    matrix = np.random.randint(-10, 10, size = (m, n), dtype = int)
    return matrix

def kha_nghich(matrix):
    try:
        kha_nghich =np.linalg.inv(matrix)
        return kha_nghich
    except:
        print("Ma trận ko vuông")
    
A = matrix(3, 4)
print(A)
print(kha_nghich(A))