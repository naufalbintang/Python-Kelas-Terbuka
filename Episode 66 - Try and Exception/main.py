import os 
from math import nan
os.system('cls')

# exception akan terjadi saat program mengalami error saat runtime

# contoh sederhana untuk menangkap exception

## contoh sederhana
# input_user = int(input('Masukkan angka: '))
# hasil = nan

# try:
#     hasil = 10 / input_user
# except:
#     print('input tidak boleh 0')

# print(f'hasil = {hasil}')

while True:
    angka = int(input('Masukkan angka pembagi: '))
    try:
        hasil = 10 / angka
        print(f'hasil = {hasil}')
        is_done = input('Apakah sudah selesai (y/n)? ')
        if is_done == 'y':
            break
    except:
        print('pembagi nol, silakan masukkan input lagi')

print('Akhir dari program.')

# contoh aplikasi untuk membuat file data.txt
try:
    with open('data.txt', 'r') as file:
        print(file.read())
except:
    print(f'File data.txt tidak ditemukan, membuat file baru')
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write('file baru')


print('akhir dari program 2')























