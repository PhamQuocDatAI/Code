import numpy as np
# Nhập ma trận 
m = np.array([[1, 2, 3], [11, 22, 33]])
print(m)

# Xem kích thước ma trận 
print(m.shape)


# VD
A = np.array([[1, 2, 0], [1, 1, 1], [2, 3, -1]])
B = np.array([[1, 1, 0], [2, 2, 2], [3, 3, 4]])
print(A*B)  # Nhân các vị trí với nhau 
print(A.dot(B)) # Phép nhân 2 ma trận 

print(np.linalg.matrix_power(A, 5)) # Tính lũy thừa ma trận 
print(A@A) # Tính A^2
print(2*np.linalg.matrix_power(A, 3) + 4*A)


# BTVN 
# Viết 1 hàm tạo 1 ma trận số nguyên có định thức = 1
# A.det() = định thức
