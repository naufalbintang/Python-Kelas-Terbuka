# Latihan Perulangan Membuat Segitiga

sisi = 10

# 1. Menggunakan For
print("===== FOR =====")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
    
# 2. Menggunakan While
print("===== WHILE =====")
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break
    
# 3. Hanya Ganjil Saja
print("===== GANJIL =====")
count = 1
while True:
    if count % 2 != 0:
        print("*"*count)
        count += 1
    else:
        count += 1
        continue
       
    if count > sisi:
        break    
    
# 4. Segitiga Sama Sisi
print("===== SAMA SISI =====")
count = 1
spasi = int(sisi / 2)
while True:
    if count % 2 != 0:
        print(" "*spasi, "+"*count)
        spasi -=1
        count += 1
    else:
        count += 1
        continue
       
    if count > sisi:
        break    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    