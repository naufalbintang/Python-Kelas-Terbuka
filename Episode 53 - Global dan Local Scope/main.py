## global dan local scope

nama_global = 'otong' # -> ini adalah variable global

# akses variable global dalam fungsi
def fungsi1():
    print(f'fungsi menampilkan: {nama_global}')
    
fungsi1()

# akses variabel global dalam loop
for i in range(0, 5):
    print(f'loop ke {i} - {nama_global}')
    
# percabangan
if True:
    print(f'if menampilkan {nama_global}')
    

## variable dan local scope 
def fungsi2():
    nama_local = 'ucup' # -> ini adalah variable local scope
    
fungsi2()
# print(nama_local) -> tidak bisa dilakukan

## contoh 1: penggunaan akses variable
def say_otong():
    print(f'hello {nama}')
    
nama = 'otong'
say_otong()

## contoh 2: mengubah variable global 
angka = 0
name = 'ucup'

def ubah(angka_baru, nama_baru):
    global angka # fungsi ini mendapat akses untuk mengubah variable angka 
    global name
    angka = angka_baru
    name = nama_baru    

print(f'angka sebelum {angka, name}')
ubah(10, 'otong')
print(f'angka setelah {angka, name}')

# contoh 3:
angka = 0

for i in range(0, 5):
    angka += i
    angka_dummy = 0
    
print(angka)
print(angka_dummy)
if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)