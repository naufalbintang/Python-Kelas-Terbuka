# copy dictionary

teman_teman = {
    "cup": "ucup surucup",
    "tong": "otong surotong",
    "dung": "dudung surudung",
    "sep": "asep si kasep",
    "cuy": "ucuy surucuy"
}

friends = teman_teman.copy()
print(f"teman-teman = {teman_teman}\n")
print(f"friends = {friends}\n")

teman_teman["cup"] = "ucup si keren"
print(f"teman-teman = {teman_teman}\n")
print(f"friends = {friends}\n")

# pop dictionary (memindahkan dari dict ke tempat lain) berdasarkan key
data_asep = friends.pop("sep")
print(f"data asep = {data_asep}")
print(f"friends = {friends}")

# pop item dictionary (item terakhir ajah)
data_terakhir = friends.popitem()
print(f"data asep = {data_terakhir}")
print(f"friends = {friends}")