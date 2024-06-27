import datetime
import os
import string
import random

data_games_template = {
    'key': 'key',
    'nama': 'nama',
    'publisher': 'publisher',
    'peak': 1_000_000,
    'rilis': datetime.datetime(1111, 1, 11)
}

data_games = {}

while True:
    os.system('clear')
    print(f'{'DATA GAMES':^20}')
    print('-'*20) 
    games = dict.fromkeys(data_games_template.keys())
    games['nama'] = input('Masukkan nama: ')
    games['publisher'] = input('Masukkan publisher: ')
    games['peak'] = int(input('Masukkan jumlah player tertinggi: '))
    
    tahun_rilis = int(input('Masukkan tahun rilis: '))   
    bulan_rilis = int(input('Masukkan bulan rilis: '))   
    tanggal_rilis = int(input('Masukkan tanggal rilis: '))   
    games['rilis'] = datetime.datetime(tahun_rilis, bulan_rilis, tanggal_rilis).strftime('%x')
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_games.update({KEY:games})
    
    print(f'{'KEY':<8}{'Nama':<19}{'Publisher':<12}{'Peak':<12}{'Rilis':<10}')
    print('-'*55)
    for KEY in data_games:
        NAMA = data_games[KEY]['nama']
        PUBLISHER = data_games[KEY]['publisher']
        PEAK = data_games[KEY]['peak']
        RILIS = data_games[KEY]['rilis']
        print(f'{KEY:<8}{NAMA:<19}{PUBLISHER:<12}{PEAK:<10,.0f}{RILIS:<10}')
        
    
    
    
    
    # break
    is_done = input('\nApakah sudah selesai (y/n)? ')
    if is_done == 'y':
        break
    else:
        None




















