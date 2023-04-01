from math import tan, pi

# game settings
WIDTH = 1200
HEIGHT = 800
# recommended fps - 60 or 90
FPS = 90
TILE = 90
# min - 8, recommended playable min - 16
MAP_SIZE = 16
MAP_SIZE = MAP_SIZE+1 if MAP_SIZE//2 else MAP_SIZE

ROOM_UP = MAP_SIZE*TILE
ROOM_DOWN = MAP_SIZE*2*TILE
ROOM_LEFT = MAP_SIZE*TILE-TILE
ROOM_RIGHT = MAP_SIZE*2*TILE-TILE*2


# player settings
player_settings = {
    'position': ((MAP_SIZE*3*TILE)//2-TILE*1.5, (MAP_SIZE*3*TILE)//2+TILE*0.5),
    'angle': 0,
    'speed': 1.3,
    'sensitivity': 0.004,
    'side': 5
}

# render settings
FOV = pi/3
HALF_FOV = FOV/2
NUM_RAYS = 1200
MAX_DEPTH = 300
DELTA_ANGLE = FOV/NUM_RAYS
DIST = NUM_RAYS / (2 * tan(HALF_FOV))
PROJ_COEF = 0.2 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
FPS_POS = (WIDTH-75, 10)
DOUBLE_PI = pi * 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 3)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
GRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
GOLDENROD_LIGHT = (161, 110, 41)
GOLDENROD = (99, 74, 27)
MAGENTA = (204, 55, 132)
