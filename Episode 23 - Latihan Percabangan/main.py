# Latihan

# Kalkulator Sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka1 = float(input("Masukkan angka 1 = "))
operator = input("Operator (+, -, x, /): ")
angka2 = float(input("Masukkan angka 2 = "))

# Percabangan
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil dari {angka1} {operator} {angka2} = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil dari {angka1} {operator} {angka2} = {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil dari {angka1} {operator} {angka2} = {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"Hasil dari {angka1} {operator} {angka2} = {hasil}")
else:
    print("operasi tidak tersedia")
    
print("Akhir dari Program")