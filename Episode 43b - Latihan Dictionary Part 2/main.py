import datetime
import os
import string
import random

# template dict mahasiswa
mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

data_mahasiswa = {}

while True:
    os.system('clear') 
    print(" ")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print(f"{'-'*20}")

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input('Nama mahasiswa: ')
    mahasiswa['nim'] = input('NIM mahasiswa: ')
    mahasiswa['sks_lulus'] = int(input('SKS Lulus: '))
    TAHUN_LAHIR = int(input('Tahun lahir (YYYY): '))
    BULAN_LAHIR = int(input('Bulan lahir (1-12): '))
    TANGGAL_LAHIR = int(input('Tanggal lahir (1-31): '))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)
    print(mahasiswa)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})
    
    print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Lahir':<10}")
    print('-'*50)
    
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']  
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x') 
        
        print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {LAHIR:<10}")

    print('\n')
    is_done = input('Sudah beres bro (y/n)? ')
    if is_done == 'y':
        break
    else:
        None
print('Akhir dari program, terimakasih.')










