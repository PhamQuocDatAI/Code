# Thư viện thao tác với tập tin và thư mục trong python: OS
import os, glob
print(dir(os)) # Các hàm có trong thư viện OS
# Liệt kê các thư mục con trong ổ đĩa 
list1 = []
list2 = []
path = 'C:\\Users\\MyPC\\Documents'
print(os.listdir(path))

print("các thư mục:")
list1 = next(os.walk(path))
print(list1)
print("")

print("các tệp:")
list2 = next(os.walk(path))
print(list2)