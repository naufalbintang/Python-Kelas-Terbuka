
# index  0(-3)   1(-2)     2(-1)
data = ["ucup", "otong", "dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir (index -1) = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")
data.insert(1, "asep")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("jajang")
print(f"data ditambah lagi = \n{data}")

# menambahkan list dengan list
data_baru = ["ujang", "usep", "dadang"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# mengubah data
# kita ubah data dengan index ke-2 menjadi michael
data[2] = "michael"
print(f"data ubah = \n{data}")

# meremove data
data.remove("ujang")
# data.remove("Usep") -> akan error karena case sensitive

# meremove data paling belakang
data.pop()
print(f"data akhir = \n{data}")

# melihat data terakhir yang diremove
data_akhir = data.pop()
print(f"data yang di remove = {data_akhir}")

