from urllib.parse import urlparse
import requests

url = input("Nhập url: ")

check = urlparse(url)
print(check)

path = check.path + check.netloc

if len(path.split('.')) < 2:
    print(f"Your input url: {url} is not valid!")
else:
    print(f"your url {url} looks good!")

# Tạo hàm kiểm tra đường link nhập vào
def input_url():
    url_start = input("Nhập url: ")
    check = urlparse(url)
    path = check.path + check.netloc
    