import random, string
def name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
n = int(input('Nhập n: '))
age = random.randrange(1,100)
dictran = dict(Name = name(n).title(), Age = age)
print(dictran)