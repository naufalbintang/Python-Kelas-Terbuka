import os
import CRUD as CRUD

if __name__ == '__main__':
    sistem_operasi = os.name
    
    
    while True:
        match sistem_operasi:
            case 'posix': os.system('clear')
            case 'nt': os.system('cls')
    
        print('SELAMAT DATANG DI PROGRAM')
        print('DATABASE PERPUSTAKAAN')
        print('=' * len('SELAMAT DATANG DI PROGRAM'))
        
        print('1. Read Data')
        print('2. Create Data')
        print('3. Update Data')
        print('4. Delete Data\n')
        
        user_option = input('Masukkan opsi: ')
        print(f'\n{'=' * len('SELAMAT DATANG DI PROGRAM')}\n')
        
        match user_option:
            case '1': print('read data')
            case '2': print('create data')
            case '3': print('update data')
            case '4': print('delete data')
            
        print(f'\n{'=' * len('SELAMAT DATANG DI PROGRAM')}\n')
        
        is_done = input('Apakah sudah selesai (y/n)? ')
        if is_done == 'y':
            break
        
    print('program berakhir, terimakasih kakaa')