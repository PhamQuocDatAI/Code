# Code tạo ngẫu nhiên n tên (n nhập từ bàn phím hoặc random) và viết hoa chữ cái đầu của tên.
# Nhận biết xem cái tên có nghĩa không?
import random, string
def name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
# Mỗi cái tên được tạo sẽ có số chữ cái ngẫu nhiên.
a = int(input('Số lượng tên: '))
Name1 =[]
Name2 =[]
while a > 0:
    n = random.randrange(1,10)
    Name1.append(name(n).title())
    Name2.append(str(name(n).title()))
    a -=1
for x in Name2:
    print(x)
# Xác định xem tên nào có ý nghĩa (Vd: John, Mary, Peter, Kalin,...)



