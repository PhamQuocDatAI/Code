def square_of_number(num1, num2, num3, num4):
    return num1**2, num2**2, num3**2, num4**2

x = square_of_number(1, 2, 3, 4)
print(x)
# Nhập 3 tham số và vẫn chạy hàm được?


dict1 = {'Nam': 20, 'Binh': 30, 'Thanh': 40}
for x in dict1:
    print("So tuoi cua %s la %d" % (x,dict1[x]))        # Cach 1
    print("So tuoi cua {1} la {0}".format(x, dict1[x])) # Cach 2
    print(f"So tuoi cua {x} la {dict1[x]}")             # Cach 3

# Dòng trắng được sử dụng trong việc ngắt đoạn code ra cho dễ đọc và tìm lỗi.
# Chúng ta sử dụng 2 dòng trắng để tạo khoảng cách giữa các hàm hoặc class top-level
# Chúng ta sẽ sử dụng một dòng trắng để tạo khoảng cách giữa các hàm trong class


# Nạp modules vào Python

import os
from matplotlib import pyplot as plt # Từ gói matplotlib chỉ lấy pyplot và đổi tên thành plt
from matplotlib import * # lấy toàn bộ hàm từ matplotlib


# Quy ước đặt tên biến, hàm, class

SO_PI = 3.14 # Hằng số phải đặt tên biến là chữ hoa
SO_E  = 2.72
bien  = 10   # Tên biến phải viết chữ thường

