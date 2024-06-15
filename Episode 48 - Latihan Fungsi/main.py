'''latihan fungsi'''

import os

# program untuk menghitung luas dan keliling persegi panjang

# # membuat header program
# os.system('cls')
# print(f'{'PROGRAM MENGHITUNG LUAS':^40}')
# print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
# print('-'*40)

# #  mengambil input user
# LEBAR = float(input('Masukkan nilai lebar: '))
# PANJANG = float(input('Masukkan nilai panjang": '))

# # program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2 * (PANJANG * LEBAR)

# # tampilkan hasilnya
# print(f'Hasil perhitungan luas = {LUAS}')
# print(f'Hasil perhitungan keliling = {KELILING}')

def header():
    '''fungsi header'''
    os.system('cls')
    print(f'{'PROGRAM MENGHITUNG LUAS':^40}')
    print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
    print('-'*40)

def input_user():
    '''fungsi mengambil input user'''
    lebar = float(input('Masukkan lebar: '))
    panjang = float(input('Masukkan panjang: '))
    return lebar, panjang

def hitung_luas(lebar, panjang):
    '''fungsi menghitung luas'''
    return lebar * panjang

def hitung_keliling(lebar, panjang):
    '''fungsi menghitung keliling'''
    return 2 * (lebar + panjang)

def display_hasil(message, value):
    '''fungsi display hasil'''
    print(f'Hasil perhitungan {message} = {value}')       
    

while True:
    header()
    
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)
    display_hasil('luas = ', LUAS)
    display_hasil('keliling = ', KELILING)
    
    
    '''break'''
    is_done = input('Apakah ingin keluar (y/n)? ')
    if is_done == 'y':
        break
    else:
        None
print('Program selesai, terima kasih')

















