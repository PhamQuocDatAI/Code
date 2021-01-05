# Line Chart
import matplotlib.pyplot as plt
import numpy as np
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c = int(input('Nhập c: '))
plt.title('Hàm số')
plt.xlabel('x')
plt.ylabel('y')
x =[]
y =[]
for n in range (-5, 5):
    x.append(n)
    y.append(a*n*n + b*n + c)
plt.plot(x,y)
print(x)
print(y)
plt.show()