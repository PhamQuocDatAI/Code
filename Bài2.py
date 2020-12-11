# Giải nhẹ nhẹ phương trình bậc nhất ^^
a = float(input('Nhập giá trị a:'))
b = float(input('Nhập giá trị b:'))
n = int(input('Nhập giá trị n:'))  
if a ==0:
    if b == 0:
        while n > 0:
            print('Phương trình ',a,'x + ',b,' = 0 có vô số nghiệm.')
            n -=1
    else:
        while n > 0:
            print('Phương trình ',a,'x + ',b,' = 0 vô nghiệm.')
            n -=1
else:
    while n > 0:
        print('Phương trình ',a,'x + ',b,' = 0 có nghiệm là: ',-b/a)
        n -=1
print('Đã giải xong.')
