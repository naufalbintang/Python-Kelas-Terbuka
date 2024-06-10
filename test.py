# faktorial

angka = int(input("Masukkan angka: "))
data_list = []
hasil = 1

if angka != 0:
    while True:
        data_list.append(angka)
        angka -= 1
        
        # break
        if angka == 0:
            break

    for i in data_list:
        print(i)
        hasil = hasil * i

    print(hasil)        
else:
    print("MasukKkan angka yang valid!")