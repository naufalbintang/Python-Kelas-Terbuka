# teknik menduplikat list

a = ["ucup", "otong", "dudung"]
print(f'a = {a}')

b = a # pass by reference
print(f'b = {b}')

# kita akan mengubah member a
a[1] = "michael"
b.sort()
print(f'a = {a}')
print(f'b = {b}')

# address dari kedua list
print(f"address a = {hex(id(a))}")
print(f"address a = {hex(id(b))}")

# menduplikat list menggunakan copy

print("membuat list c dengan a.copy()")
c = a.copy() # full duplicate (data baru)
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

print("kita ubah data 0")
c[0] = "dadang"
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

print("kita ubah data 1")
a[1] = "otong"
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
