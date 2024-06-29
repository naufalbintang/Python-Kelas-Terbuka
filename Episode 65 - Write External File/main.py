import os
os.system('cls')

# 1. mode write 
# dia akan membuat file baru jika tidak ada
# lalu akan menimpa atau overwrite isi sebelumnya

with open("data1.txt", 'w', encoding='utf-8') as file:
    file.write('Jhon Si Jhonny')

with open("data1.txt", 'w', encoding='utf-8') as file:
    file.write('Ucup Surucup')

with open("data1.txt", 'w', encoding='utf-8') as file:
    file.write('overwrite')


# 2. mode append
with open("data2.txt", 'w', encoding='utf-8') as file:
    file.write('Jhon Si Jhonny\n')

with open("data2.txt", 'a', encoding='utf-8') as file:
    file.write('Ucup Surucup\n')

with open("data2.txt", 'a', encoding='utf-8') as file:
    file.write('tambah lagi dengan append\n')


# 3. mode r+

with open('data3.txt', 'w', encoding='utf-8') as file:
    file.write('data ke 3\n')

with open('data3.txt', 'r+', encoding='utf-8') as file:
    file.write('baris 1\n')
    file.write('baris 2\n')
    file.write('baris 3\n')

with open('data3.txt', 'r+', encoding='utf-8') as file:
    data = file.read()
    print(data)

with open('data3.txt', 'r+', encoding='utf-8') as file:
    file.write('otong surotong') # menimpa isi text sesuai dengan panjang data



    
    



