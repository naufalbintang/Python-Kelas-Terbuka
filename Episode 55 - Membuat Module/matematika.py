# module matematika

def tambah(*args):
    hasil = 0
    for i in args:
        hasil += i

    return hasil


def kali(*args):
    hasil = 1
    for i in args:
        hasil *= 1
        
    return hasil

def pangkat(n: int):
    return lambda angka: angka ** n