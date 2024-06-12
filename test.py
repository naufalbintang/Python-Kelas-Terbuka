import datetime

game1 = {
    'nama': 'CSGO',
    'publisher': 'Valve',
    'steam': True,
    'peak_player': 1_519_457,
    'tanggal_rilis': datetime.datetime(2012, 8, 21),
}

game2 = {
    'nama': 'Genshin Impact',
    'publisher': 'Hoyolab',
    'steam': False,
    'peak_player': 63_000_000,
    'tanggal_rilis': datetime.datetime(2020, 9, 28)
}

game3 = {
    'nama': 'Honkai Star Rail',
    'publisher': 'Hoyolab',
    'steam': False,
    'peak_player': 24_000_000,
    'tanggal_rilis': datetime.datetime(2023, 4, 26)
}

game4 = {
    'nama': 'Dota 2',
    'publisher': 'Valve',
    'steam': True,
    'peak_player': 1_295_114,
    'tanggal_rilis': datetime.datetime(2009, 7, 9)
}
game5 = {
    'nama': 'League of Legends',
    'publisher': 'Riot Games',
    'steam': False,
    'peak_player': 8_000_000,
    'tanggal_rilis': datetime.datetime(2009, 10, 27)
}

data_games = {
    'GAME001': game1,
    'GAME002': game2,
    'GAME003': game3,
    'GAME004': game4,
    'GAME005': game5,
}

print(f'{'key':<8} {'Nama':<18} {'Publisher':<11} {'Steam':<6} {'Peak Players':<13} {'Tanggal Rilis':<8}')
print(f'-'*74)

for KEY in data_games:
    NAMA = data_games[KEY]['nama']
    PUBLISHER = data_games[KEY]['publisher']
    STEAM = data_games[KEY]['steam']
    PEAK_PLAYERS = data_games[KEY]['peak_player']
    TANGGAL_RILIS = data_games[KEY]['tanggal_rilis'].strftime('%x')
    
    print(f'{KEY:<8} {NAMA:<18} {PUBLISHER:<11} {STEAM:^6} {PEAK_PLAYERS:<13,.0f} {TANGGAL_RILIS:<8}')
    


























