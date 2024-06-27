import os

daftar_nilai = {
    'PU': 601.28,
    'PK': 710.42,
    'PPU': 756.46,
    'PBM': 684.21,
    'LBI': 649.63,
    'LBE': 743.87,
    'PM': 677.61,
}

os.system('cls')
print(f'{'RATA - RATA NILAI UTBK':^24}')
print('='*24)

for key in daftar_nilai:
    nilai = daftar_nilai[key]
    print(f'{key}\t\t= {nilai}')

def rata2_nilai(pu, pk, ppu, pbm, lbi, lbe, pm):
    hasil = (pu + pk + ppu + pbm + lbi + lbe + pm) / 7
    return hasil

rata_rata = rata2_nilai(daftar_nilai['PU'], daftar_nilai['PK'], daftar_nilai['PPU'], daftar_nilai['PBM'], daftar_nilai['LBI'], daftar_nilai['LBE'], daftar_nilai['PM'])
print(f'Rata - rata\t= {rata_rata:.2f}\n\n\n')





















