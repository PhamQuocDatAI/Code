import random
a = random.randrange(50, 1000)
e = random.randrange(50, 1000)
print('List của bạn có ', a,' phần tử.')
list1 = []
list2 = []
while a >0:
    b = random.randrange(-1000, 1000)
    list1.append(b)
    list2.append(str(b))
    a -=1
print(','.join(list2))
list3 =[]
list4 =[]
while e >0:
    c = random.uniform(-1000, 1000)
    list3.append(c)
    list4.append(str(c))
    e -=1
print(','.join(list4))