import os
# Nhập dung lượng folder từ bàn phím 
n = float(input('Nhập size folder: '))
print('Folder có dung lượng là ',n,' MB.')
# Tạo chuỗi kí tự 
def randomstr(): 
    name = random.choice(string.ascii_letters)
    for i in range(1023999):
        name += random.choice(string.ascii_letters)
    return name
# Tính xem có bao nhiêu file nguyên 1000KB và dư 1 file lẻ
a = n * 1024 // 1000
b = n * 1024 % 1000
print('Số file là: ', a)
# Giới hạn dung lượng file là 1000KB
path = 'C://Users//PC//Desktop//Bai 13-3'
while a > 0:
    # Tạo tập tin trong folder Bai 13-3
    ten_tap_tin = input('Nhập tên tập tin: ')
    textfile = os.path.join(path, ten_tap_tin + '.txt')
    size = 1024000
    # Làm sao để ghi n file mà size file = 1000KB thì dừng và chuyển sang file khác
    file1 = open(textfile, 'w+')
    # Sinh nội dung ngẫu nhiên, không phải nhập bàn phím
    
    file1.write(input('Nội dung: '))
    file1.write('\0' * size)
    file1.close()
    a -= 1
# Dùng vòng lặp để ghi vào đủ 1000KB vào file
# Tương tự để ghi file lẻ còn lại
# Lấy file size của folder Bai 13-3
def file_size(ten_file):
    return os.stat(ten_file).st_size

ten_file = input('Nhập tên file: ')
size = file_size(ten_file)
print('file size ', size)
# Tính tổng của các file trong folder Bai 13-3 
def sum_size_file(path):
    t = 0
    for e in os.scandir(path):
        if e.is_dir():
            t = t + sum_size_file(e.path)
        else:
            t = t + e.stat().st_size
    return(t)

t = sum_size_file('') # Địa chỉ folder 13-3
print('Size' , t)                
