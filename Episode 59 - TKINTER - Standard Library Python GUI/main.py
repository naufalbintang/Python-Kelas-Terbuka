# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg = 'white') # -> warna background
window.geometry('300x200') # -> ukuran window
window.resizable(False, False) # -> resize window
window.title('Sapa Dia!') # -> judul program

# variable dan function
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()
def tombol_klik():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f'Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteengg!'
    showinfo(title = 'Whazzup!', message = pesan)

# frame input
input_frame =  ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx = 10, pady = 10, fill = 'x', expand = True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text = 'Nama Depan: ')
nama_depan_label.pack(padx = 10, fill = 'x', expand = True)
# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable = NAMA_DEPAN)
nama_depan_entry.pack(padx = 10, fill = 'x', expand = True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text = 'Nama belakang: ')
nama_belakang_label.pack(padx = 10, fill = 'x', expand = True)
# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable = NAMA_BELAKANG)
nama_belakang_entry.pack(padx = 10, fill = 'x', expand = True)
# 5. Tombol
tombol_sapa = ttk.Button(input_frame, text = 'Sapa!', command = tombol_klik)
tombol_sapa.pack(fill = 'x', expand = True, pady = 10, padx = 10)

# main loop window
window.mainloop()




























































