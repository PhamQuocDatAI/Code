# Tạo 1 list gồm các số ngẫu nhiên rồi tìm giá trị lớn nhất trong list (Ko dùng hàm max)
import random
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
