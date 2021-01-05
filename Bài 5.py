# Tạo 1 list (bằng tay) -> Truy xuất các phần tử trong list 
list1 = [1, 3, 5, 7, -50, -123.123, 487.9273, 123456]
for index, x in enumerate(list1):
    print(index ,'--', x)



# Tạo 1 list với các giá trị ngẫu nhiên trong phạm vi [a,b] với a,b nhập từ bàn phím
    # Số lượng phần tử của list nhập từ bàn phím

import random   
n = int(input('Bạn muốn list có bao nhiêu phần tử: '))
if n <= 0:
    print('Số phần tử của list không nhận giá trị âm. Nhập lại')
    n = int(input('Bạn muốn list có bao nhiêu phần tử: '))
a = int(input('Nhập giá trị đầu trong đoạn: '))
b = int(input('Nhập giá trị cuối trong đoạn: '))
c = int(input('Step: '))
while a>=b:
    print('Bạn nhập giá trị đầu lớn hơn giá trị cuối. Hãy nhập lại: ')
    a = int(input('Nhập giá trị đầu trong đoạn: '))
    b = int(input('Nhập giá trị cuối trong đoạn: '))
list1 =[]
list2 =[]
if n<0:
    n==abs(n)
if a==b:
    print('Giá trị lớn nhất trong dãy là:',a)
else:
    if a>b:
        while n>=0:
            d = random.randrange(b,a,c)
            list1.append(d)
            list2.append(str(d))
            n -=1
        print(','.join(list2))
    else:
        while n>=0:
            d = random.randrange(a,b,c)
            list1.append(d)
            list2.append(str(d))
            n -=1
        print(','.join(list2))
    max = list1[0]
    for x in list1:
        if max < x:
            max = x
print('Giá trị lớn nhất là:',max)


