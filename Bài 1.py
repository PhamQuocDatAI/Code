# Bài 1: Nhập từ bàn phím 2 số nguyên và tính

a = int(input('Nhập số nguyên a = '))
b = int(input('Nhập số nguyên b = '))
print('Tổng hai số là: a + b =', a+b)
print('Tích hai số là: a * b =', a*b)
print('Hiệu hai số là: a - b =', a-b)
if b !=0:
    print('Phần dư của a/b là: ', a%b)
    print('Phần nguyên của a/b là: ', a//b)
else:
    print('Không tìm được phần dư của a/b.')
    print('Không tìm được phần nguyên của a/b')


# Bài 2: Nhập từ bàn phím 2 số thực và tính

a = float(input('Nhập số thực a = '))
b = float(input('Nhập số thực b = '))
print('Tổng hai số a,b là: ', a+b)
print('Tích hai số a,b là: ', a*b)
print('Hiệu của hai số a,b là: ', a-b)
if b !=0: 
    print('Thương của hai số a,b là: ', a/b)
else:
    print('Không thực hiện được phép chia.')

# Bài 3: Sử dụng hàm toán, nhập 1 số từ bàn phím và tính

a = float(input('Nhập số a = '))
import math
print('Trị tuyệt đối của a là: ', abs(a))
print('Phần nguyên của a là: ', math.trunc(a))
print('Chuyển đổi ', a,' thành số thực: ', float(a))
b = float(input('Nhập số b = '))
print('Lũy thừa x^y là: ', math.pow(a,b))
if a >= 0:
    print('Căn bậc 2 của a là: ', math.sqrt(a))
else:
    print('Không có căn bậc 2 của ', a)
if b >= 0:
    print('Căn bậc 2 của b là: ', math.sqrt(b))
else:
    print('Không có căn bậc 2 của ', b)


# Bài 4: Nhập hai số từ bàn phím và so sánh 2 số
a = float(input('Nhập a = '))
b = float(input('Nhập b = '))
print('a >= b', a >= b)
print('a <= b', a <= b)
print('a > b', a > b)
print('a < b', a < b)
print('a != b', a != b)


# Bài 5: Nhập 1 chuỗi kí tự từ bàn phím
import string
a = str('Good morning, teacher!')
print('Chuyển chuỗi a thành in hoa:', a.upper())
print('Chuyển chuỗi a thành in thường:', a.lower())


# Bài 6: Xuất ra màn hình 1 chuỗi ký tự nằm trên nhiều hàng
import string
print('''But you understand, understand when it hurts 
         You sympathize, when my heart's 'bout to burst
         I like you 'cause you're sad like me
         I guess misery loves company''')


