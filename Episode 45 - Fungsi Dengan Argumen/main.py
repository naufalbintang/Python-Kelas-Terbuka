'''Fungsi dengan argumen'''



# def nama_fungsi(argument):
#     badan fungsi

def hello_world(nama):
    '''fungsi hello_world menerima input dengan variabel nama'''
    print(f'Selamat datang dunia wahai {nama}')

hello_world('ucup')
hello_world('asep')


# program tambah
def tambah(angka_1, angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')

tambah(1, 5)
tambah(10000, 1)

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f'Yang terhormat {peserta}')

annggota_boyband = ['ucup', 'otong', 'dudung']
say_hi(annggota_boyband)




















