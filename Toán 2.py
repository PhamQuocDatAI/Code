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

# Viết 1 hàm tạo ma trận random cấp n có detA != 0 
# Viết 1 hàm tạo ma trận random cấp n có detA != 0 (n nhập từ bàn phím)


# Viết 1 hàm
# Input: --> n: int
# Output: 
    # print ma trận random cấp n 
    # Định thức của ma trận 
    # Hạng của ma trận 
    # Tính A^2, A^3

import numpy as np
import random
def matrix(n):
    
>>>>>>> f6c94c44a28fcdc72943eb4ddd4aacfd707de2e9
