#Các thư viện cần thiết
import requests, re
from bs4 import BeautifulSoup


#Các hàm cần thiết

#Hàm đọc nội dung của trang web theo url chỉ định
#Kết quả trả về là 1 văn bản dạng chuỗi
def doc_noi_dung(url):
    # Gửi yêu cầu truy cập url
    raw_page = requests.get(url)
    # Lấy code html của trang web được trả về theo url
    content = BeautifulSoup(raw_page.text, "html.parser")
    return content

#Hàm lấy các đường link web trong nội dung đọc về
#Kết quả trả về là 1 list chứa các đường link
def lay_cac_duong_link(content):
    a_tags = content.find_all("a")
    result = []
    for item in a_tags:
        link = item.get("href")
        result.append(link)
    return result

#Hàm kiểm tra tính hợp lệ của 1 đường link và chỉnh sửa link
#Kết quả trả về: True nếu hợp lệ, False nếu không hợp lệ
def check_and_fix(link):
    cho_duyet = lay_cac_duong_link(content)
    da_duyet = []
    for item in cho_duyet:
        kiem_tra = re.search(r'^https://', item)
        if kiem_tra:
            da_duyet.append(y)
        else:
            y = "https://vietnamnet.vn" + y
            da_duyet.append(y)
    return da_duyet
