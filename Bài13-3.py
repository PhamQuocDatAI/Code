import string , random , os
def randomstr(): 
    name = random.choice(string.ascii_letters)
    for i in range(1023999):
        name += random.choice(string.ascii_letters)
    return name
path = 'C://Users//PC//Desktop//Bai 13-3' + '//'
os.mkdir(path)
os.chdir(path)
#Dung lượng dữ liệu giới hạn:
size = float(input('Nhập dung lượng dữ liệu (1MB-1024MB):'))
so_file_nguyen = size*1024//1000
file_du = size * 1024 % 1000        
# Tạo file nguyên với kích thước mỗi file là 1000KB
for i in range(int(so_file_nguyen)):
    f = 'file'+str(i)+'.txt'
    f = open(f, mode= 'w')
    f.write(randomstr())
    f.close()
#Tạo 1 file với số byte còn lại
if  file_du > 0:
    f = 'file'+ str(n) +'.txt'
    f = open(f, mode= 'w')
    name = random.choice(string.ascii_letters)
for i in range(file_du):
    name += random.choice(string.ascii_letters)
    f.write(name)
    f.close()
    file_du += 1
