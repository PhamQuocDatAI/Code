# Thư viện thao tác với tập tin và thư mục trong python: OS
import os, glob
print(dir(os)) # Các hàm có trong thư viện OS
# Liệt kê các thư mục con trong ổ đĩa 
list1 = []
list2 = []
path = 'C://Users//PC//Desktop//ENGBREAKING'
for root, dirs, files in os.walk(path):
    ten_tap_tin = glob.glob(path)
    list1.append(ten_tap_tin)
    ten_thu_muc = os.path.dirname(path)
    list2.append(ten_thu_muc)
print(list1)
print(list2)

