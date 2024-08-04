from . import Operasi

def delete_console():
    read_console()
    while True:
        print('Silakan pilih nomor buku yang akan didelete')
        no_buku = int(input('No buku: '))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]
        
        
            # data yang ingin diupdate
            print('\n' + '=' * 100)
            print('Data yang ingin anda hapus')
            print(f'1. Penulis\t: {penulis:.40}')
            print(f'2. Judul\t: {judul:.40}')
            print(f'3. Tahun\t: {tahun:4}')

            is_done = input('Apakah anda yakin (y/n)? ')
            if is_done == 'y':
                Operasi.delete(no_buku) 
                break
        else:
            print('Nomor tidak valid, silakan masukkan lagi')
    print('Data berhasil dihapus')

def update_console():
    read_console()
    while True:
        print('Silakan pilih nomor buku yang akan diupdate')
        no_buku = int(input('No buku: '))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            break
        else:
            print('Nomor tidak valid, silakan masukkan lagi')
            
    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]
    
    while True:
        # data yang ingin diupdate
        print('\n' + '=' * 100)
        print('Silakan pilih data apa yang ingin anda ubah')
        print(f'1. Penulis\t: {penulis:.40}')
        print(f'2. Judul\t: {judul:.40}')
        print(f'3. Tahun\t: {tahun:4}')
    
        # memilih mode untuk update
        user_option = input('Pilih data [1, 2, 3]: ')
        match user_option:
            case '1': penulis = input('Penulis\t: ')
            case '2': judul = input('Judul\t: ')
            case '3': 
                while True:
                    try:
                        tahun = int(input('Tahun\t: '))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print('tahun harus angka, silakan masukkan tahun lagi (yyyy)')
                    except:
                        print('tahun harus angka, silakan masukkan tahun lagi (yyyy)')
            case _: print('index tidak cuocuoookkk')
        
        print('Data baru anda')
        print(f'1. Penulis\t: {penulis:.40}')
        print(f'2. Judul\t: {judul:.40}')
        print(f'3. Tahun\t: {tahun:4}')
        
        is_done = input('Apakah data sudah sesuai (y/n)? ')
        if is_done == 'y':
            break
    
    Operasi.update(no_buku, pk, data_add, penulis, judul, tahun)
    
def create_console():
    print('\n\n' + '=' * 100)
    print('Silakan tambah data buku\n')
    penulis = input('Penulis\t: ')
    judul = input('Judul\t: ')
    while True:
        try:
            tahun = int(input('Tahun\t: '))
            if len(str(tahun)) == 4:
                break
            else:
                print('tahun harus angka, silakan masukkan tahun lagi (yyyy)')
        except:
            print('tahun harus angka, silakan masukkan tahun lagi (yyyy)')

    Operasi.create(tahun, judul, penulis)
    print('\nBerikut adalah data baru anda.')
    read_console()
    
def read_console():
    data_file = Operasi.read()
    index = 'No'
    judul = 'Judul'
    penulis = 'Penulis'
    tahun = 'Tahun'
    
    # header
    print('\n' + '=' * 100)
    print(f'{index:4} | {judul:40} | {penulis:40} | {tahun:5}')
    print('-' * 100)
    
    # data
    for index, data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f'{index + 1:4} | {judul:.40} | {penulis:.40} | {tahun:4}', end='')
        
        
    
    # footer``
    print('=' * 100 + '\n')