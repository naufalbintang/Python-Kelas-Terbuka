rumus_map = {
    "1": lambda sisi: sisi**2, # persegi
    "2": lambda panjang, lebar: panjang * lebar, # persegi panjang
    "3": lambda atas, alas, tinggi: (atas + alas) * tinggi / 2,
    "4": lambda radius: 22 / 7 * radius, #lingkaran
}

satuan_map = {
    "km": "kilometer",
    "hm": "hektometer",
    "dam": "dekameter",
    "m": "meter",
    "dm": "desimeter",
    "cm": "centimeter",
    "mm": "milimeter",
}
    
    
while True:
    print("""
    1. Persegi
    2. Persegi Panjang
    3. Trapesium
    4. Lingkaran  
    """)

    operasi = str(input("Masukkan operasi yang ingin dilakukan: "))
    
    # persegi
    if operasi == "1":
        sisi = float(input("Masukkan panjang sisi: "))
        satuan = str(input("Masukkan satuan: "))
        if satuan.lower() in satuan_map:
            print(f"{sisi} x {sisi} = {rumus_map["1"](sisi)}")
    
    # persegi panjang
    elif operasi == "2":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        satuan = str(input("Masukkan satuan: "))
        if satuan.lower() in satuan_map:
            print(f"{panjang} {satuan} x {lebar} {satuan} = {rumus_map["2"](panjang, lebar)} {satuan_map[satuan]}")
    
    # trapesium
    elif operasi == "3":
        atas = float(input("Masukkan panjang atas: "))
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        satuan = str(input("Masukkan satuan: "))
        if satuan.lower() in satuan_map:
            print(f"({atas} {satuan} + {alas} {satuan}) x {tinggi} {satuan} / 2 = {rumus_map["3"](atas, alas, tinggi)} {satuan_map[satuan]}")
            
    # lingkaran
    elif operasi == "4":
        radius = float(input("Masukkan radius: "))
        satuan = str(input("Masukkan satuan: "))
        if satuan.lower() in satuan_map:
            print(f"22 / 7 x {radius} {satuan} x {radius} {satuan} = {rumus_map["4"](radius):.2f} {satuan_map[satuan]}")        
        
    # break
    is_keluar = str(input("\nApakah ingin keluar (y/n)?"))
    if is_keluar == "y":
        break
    elif is_keluar == "n":
        None
    else:
        print("Unknown Input")
        break
    
    
    
    
    
    
    
    
    
    

        

