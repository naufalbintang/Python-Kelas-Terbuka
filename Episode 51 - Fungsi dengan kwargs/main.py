'''**kwargs'''

def fungsi(nama, tinggi, berat):
    '''fungsi biasa'''
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
    
fungsi('ucup', 183, 79)

def fungsi(**kwargs):
    '''fungsi biasa'''
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
    
fungsi(nama = 'ucup', tinggi = 183, berat = 79)

# studi kasus
def math(*args, **kwargs):
    if kwargs['option'] == 'tambah':
        output = 0
        for angka in args:
             output += angka
    elif kwargs['option'] == 'kali':
        output = 1
        for angka in args:
             output *= angka
    else:
        print('tidak ada operasi')
    
    return output
    
tambah = math(1, 2, 3, 4, option = 'tambah')
kali = math(1, 2, 3, 4, option = 'kali')
print(f'hasil tambah = {tambah}')
print(f'hasil kali = {kali}')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    