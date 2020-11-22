# Tạo list gồm các số nguyên ngẫu nhiên trong đoạn cho trước
import random
n = int(input('Bạn muốn list có bao nhiêu phần tử: '))
a = int(input('Nhập giá trị đầu trong đoạn: '))
b = int(input('Nhập giá trị cuối trong đoạn: '))
if a>b:
    print('Bạn nhập giá trị đầu lớn hơn giá trị cuối:')
    

list1 =[]
list2 =[]
if n<0:
    n==abs(n)

else:
    while n>=0: 
        d = random.randrange(a,b)
# In ra các giá trị trong list được tạo ngẫu nhiên
        list1.append(d)
        list2.append(str(d))
        n -=1
print(','.join(list2))
# Tìm giá trị lớn nhất trong list đã được tạo trên
max = list1[0]
for x in list1:
    if max < x:
        max = x
print('Giá trị lớn nhất là:',max)
