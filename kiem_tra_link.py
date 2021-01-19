import re

linkpage = ["/vn/thoi-su/bang-tuyet-xuat-hien-nhieu-noi-o-mien-bac-704516.html",
            "/vn/kinh-doanh/thi-truong/gia-bia-nuoc-ngot-tang-703816.html",
            "/vn/thoi-su/an-toan-giao-thong/",
            "/vn/thoi-su/an-toan-giao-thong/van-con-70-000-ve-tau-tet-phat-nghiem-xe-khach-tang-gia-qua-cao-706565.html",
            "/en/business/researchers-warn-of-risks-for-vietnam-in-2021-706482.html?"]

lich_su1 = []

for index, y in enumerate(linkpage):
  test1 = re.search(r'^https://', y)
  if test1:
    lich_su1.append(y)
  else:
    y = "https://vietnamnet.vn" + y
    lich_su1.append(y)
print("-"*300)
print(lich_su1)
print("Nộp bài ^-^")


