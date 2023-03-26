from settings import *
from random import randint


def wall_chance(text_map, row, symbol):

    # Empty center of map
    map_center = tuple(
        (i for i in range(int(MAP_SIZE/2-3), int(MAP_SIZE/2+2))))
    if row in map_center and symbol in map_center:
        return 0

    # No more 3 walls in row by horizontal
    if symbol > 3:
        three_previous_squares = text_map[row][symbol-3:symbol]
        if all(i == 'W' for i in three_previous_squares):
            return 0

    # No more 3 walls in row by vertical
    if row > 3:
        three_upper_squares = []
        for i in range(3):
            three_upper_squares.append(text_map[row-i][symbol-1])
        if all(i == 'W' for i in three_upper_squares):
            return 0

    # Standart wall chance
    wall_chance = 3
    # Biggest wall chance if previous square is a wall
    if text_map[row][symbol-1] == 'W':
        wall_chance += 3
    # Biggest wall chance if upper square is a wall
    if text_map[row-1][symbol] == 'W':
        wall_chance += 3

    return wall_chance


def map_generate():
    text_map = []
    # up row of walls (edge of world)
    text_map.append('W'*MAP_SIZE)

    for row in range(1, MAP_SIZE-1):
        # left row of walls (edge of world)
        text_row = 'W'
        for symbol in range(1, MAP_SIZE-1):
            chance = wall_chance(text_map, row-1, symbol)
            text_row += 'W' if randint(1, 20) <= chance else '.'
        # right row of walls (edge of world)
        text_row += 'W'

        text_map.append(text_row)

    # down row of walls (edge of world)
    text_map.append('W'*MAP_SIZE)
    return text_map


# create world map
text_map = map_generate()

# research coords of walls
world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i*TILE, j*TILE))
