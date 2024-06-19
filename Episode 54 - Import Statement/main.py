# import

# fungsinya adalah untuk mengambil program dari file eksternal .py

# 1. untuk menyambungkan program eksternal
import program_print
import program_si_ucup

# 2. import dengan data
import variable
import kucuy

# data ada di namespace variable
print(variable.data)
print(kucuy.data)

# 3. import dengan fungsi
import matematika
hasil = matematika.tambah(4, 5)
print(hasil)