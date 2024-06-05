# program list buku

list_buku = []
while True:
    print("\nMasukkan data buku")
    judul = input("Judul buku\t: ")
    penulis = input("Nama penulis\t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    print(list_buku)

    print("\n", "="*15, "Data Buku", "="*15)
    for index, buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}" )

    print("\n", "="*20)
    lanjut = input("Apakah ingin lanjut? (y/n): ")
    if lanjut == "n":
        break

print("PROGRAM SELESAI")







