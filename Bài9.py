import os, time
check = input('Bạn có muốn tắt máy không? (Có/Không):')
while check =='Không' or check =='No':
    time.sleep(30)
    check = input('Bạn có muốn tắt máy không? (Có/Không):')
else:
    os.system('Shutdown /s')

