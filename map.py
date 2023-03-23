from settings import *

text_map = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'W..WWW..................W......W',
    'W.W....W.......WWW.........W...W',
    'W.W.....W........WW.......WW...W',
    'W.W.WW.WW......................W',
    'W............WW....WW....W.....W',
    'W......WWW....WW..WW....WWWWW..W',
    'W.WW.....W.................W...W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i*TILE, j*TILE))
