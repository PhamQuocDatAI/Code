import numpy as np
import random
n = int(input("Nhập giá trị n: "))
# Tạo ma trận số nguyên cấp n ngẫu nhiên trong phạm vị cho trước
A = np.random.randint(-10, 10, (n, n))
print(A)
# Tính detA
print("Hạng của ma trận A: ", int(np.linalg.det(A)))
# Tính A^2, A^3
print("A^2 = ", A@A)
print("A^3 = ", (A@A)@A)






