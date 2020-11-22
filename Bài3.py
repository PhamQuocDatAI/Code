# Chương trình chạy For loop với list
fruits = ['apple','banana','peach','watermelon']
for x in fruits:
    if x =='peach':
        print('I love peach.')
        break
    else:
        print('i hate',x)

# Chương trình in ra các số chẵn trong list cho trước    
numbers =[1,3,5,7,12,14,25,37,555,1000]
a = []
i =0
for y in numbers:
    if y%2 == 0:
        a.append(y)
        i+=1
print('Các số chẵn trong dãy là:',a[0:])

# Thay đổi bước nhảy của For loop
for k in range(10,20,2):
    print('Python')
for m in range(10,20,3):
    print('Phương pháp 10k ^.^')
