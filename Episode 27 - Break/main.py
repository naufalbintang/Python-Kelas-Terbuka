# break
angka = 0

data_int = int(input("Hitung sampai: "))

while True:
    angka += 1
    print(f"count = {angka}")
    
    if angka == data_int:
        print("nice!")
        break
    print("whassup!")
print("cukup")