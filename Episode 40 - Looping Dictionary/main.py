# looping dictionary

teman_teman = {
    "cup"   : "ucup surucup",
    "tong"  : "otong surotong",
    "dung"  : "dudung surudung",
    "sep"   : "asep si kasep",
    "cuy"   : "ucuy surucuy",
}

# looping first try (yang keluar hanya key nya)
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item atau iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)
    
items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f"key = {key}, value = {value}")








