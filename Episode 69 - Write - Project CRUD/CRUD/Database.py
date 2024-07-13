from . import Operasi

DB_NAME: str = 'data.txt'
TEMPLATE: dict = {
    'pk': 'XXXXXX',
    'date_add': 'yyyy-mm-dd',
    'judul': 255 * ' ',
    'penulis': 255 * ' ',
    'tahun': 'yyyy'
}

def init_console():
    try:
        with open(DB_NAME, 'r') as file:
            print('Database tersedia, init done!')
    except:
        print('Database tidak ditemukan, silakan buat database baru.')
        Operasi.create_first_data()








































    