from . import Operasi

def read_console():
    data_file = Operasi.read()
    index = 'No'
    judul = 'Judul'
    penulis = 'Penulis'
    tahun = 'Tahun'


    # header
    print('\n' + '=' * 100)
    print(f'{index:4} | {judul:30} | {penulis:30} | {tahun:5}')
    print('-' * 100)

    # data
    for index, data in enumerate(data_file, 1):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f'{index:4} | {judul:.30} | {penulis:.30} | {tahun:4}', end='')

    # footer
    print(f'{'=' * 100}\n')
    
    
    

    
    
    
    