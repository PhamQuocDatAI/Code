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
n = int(input("Nhập giá trị n: "))
A = np.random.randint(-10, 10, (4, 4))
print(A)