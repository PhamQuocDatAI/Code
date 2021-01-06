import os
print("tất cả các tệp và thư mục trong ổ C:")
path = 'C:\\Users\\MyPC\\Documents'
print(os.listdir(path))
print("")

print("các thư mục:")
list1 = next(os.walk(path))
print(list1)
print("")

print("các tệp:")
list2 = next(os.walk(path))
print(list2)