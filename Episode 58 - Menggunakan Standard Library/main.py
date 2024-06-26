import datetime

data_waktu = datetime.datetime.now()
print(f'datetime now: {data_waktu}')
print(f'tahun: {data_waktu.year}')
print(f'hari: {data_waktu.strftime("%A")}')

from collections import Counter

data: list[str] = ['a', 'b', 'c', 'd', 'a', 'd', 'a']
data_count: dict = Counter(data)
print(f'data count = {data_count}') 
print(f'jumlah a = {data_count['a']}') 

import io
file = io.open('file_text.txt', 'r')
print(file.read())
