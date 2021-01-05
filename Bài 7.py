# Tìm được giá trị nhỏ nhất, lớn nhất của list. 
import random
n = int(input('Số phần tử của list: '))
list1 =[]
list2 =[]
while n>=0:
    a =random.uniform(1, 20)
    list1.append(a)
    list2.append(str(a))
    n -=1
print(','.join(list2))
min = list1[0]
for x in list1:
    if min > x:
        min == x
print('Giá trị nhỏ nhất là:',min)
# Sắp xếp list
