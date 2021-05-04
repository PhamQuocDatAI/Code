import re, requests, os, codecs, time
from bs4 import BeautifulSoup


# Hàm lấy thông tin từ 1 trang web 
def doc_noi_dung(url):
    raw_page = requests.get(url)
    content = BeautifulSoup(raw_page.text, "html.parser")
    return content

# Hàm tìm lọc các link a href
def link_page(content):
    a_tags = content.find_all("a")
    result = []
    for item in a_tags:
        link = item.get("href")
        result.append(link)
    return result

# Hàm chỉnh sửa link 
def kiem_tra_link(item):
    link = str(item)
    regex = re.compile(r'^(http://|https://|/vn)')
    result = re.match(regex, link) is not None
    return result

# Hàm tạo thư mục
def folder():
    name = input("ten folder: ")
    os.mkdir(name)
    os.chdir(name)

# Hàm lưu nội dung 
def luu_file(url, stt):
    f = codecs.open('file' + str(stt) + '.html', 'w', 'utf8')
    f.write(requests.get(url).text)
    f.close()

start_time = time.time()
max_page = int(input("Nhập số trang cần crawler: "))
count = 0
raw_link = []
full_link = ["https://vietnamnet.vn"]

while (count < max_page) and (len(full_link) > 0):
    url = full_link.pop(0)
    page = doc_noi_dung(url)
    links = link_page(page)
    for item in links: 
        if kiem_tra_link(item) == True:
            raw_link.append(item)
    for item in raw_link:
        test = re.search(r'^https://|http://', item)
        if test:
            pass
        else:
            item = "https://vietnamnet.vn/" + item
            if not(item in full_link):  
                full_link.append(item) 
    count += 1

# In ra màn hình các đường link (có thể có hoặc không)
for index, z in enumerate(full_link, 1):
    print(index,": ", z)

folder()

n = int(input("Số link muốn tải về máy: "))
download_link = full_link[0:n]
for index, x in enumerate(download_link):
    luu_file(x, index)


print("--- %s seconds ---" % (time.time() - start_time))