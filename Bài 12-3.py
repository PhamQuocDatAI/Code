import random, string
def name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
n = random.randrange(50,101)
a = random.randrange(1,10)
age = random.randrange(1,200)
print(n,'--',a)
dic = []
while n > 0:
    dic1 = dict(Name = name(a), Age = age)
    dic.append(dic1)
    n -=1
print(dic)

