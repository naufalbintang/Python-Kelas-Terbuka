def tambah(*args) -> float:
    hasil = 0
    for angka in args:
        hasil += angka
    return hasil

def kali(*args) -> float:
    hasil = 1
    for angka in args:
        hasil *= angka
    return hasil