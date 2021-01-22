import requests
from bs4 import BeautifulSoup
import re


url = input("Nhập url cần crawler: ")
def doc_noi_dung(url):
    # Gửi yêu cầu truy cập url
    raw_page = requests.get(url)
    # Lấy code html của trang web được trả về theo url
    content = BeautifulSoup(raw_page.text, "html.parser")
    return content

content = doc_noi_dung(url)
def link_page(content):
    a_tags = content.find_all("a")
    result = []
    for item in a_tags:
        link = item.get("href")
        result.append(link)
    return result

A = link_page(content)
#print("---"*300)
#print(A)
lich_su = []

for index, y in enumerate(link_page(content)):
  #print(index, "--", y)
  test = re.search(r'^https://', y)
  if test:
    lich_su.append(y)
  else:
    y = "https://vietnamnet.vn" + y
    lich_su.append(y)
print("--"*300)
print(lich_su)