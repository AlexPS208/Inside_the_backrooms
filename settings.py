from math import tan, pi

# game settings
WIDTH = 1200
HEIGHT = 800
# recommended fps - 60 or 90
FPS = 90
TILE = 90
# min - 2, recommended playable min - 16
MAP_SIZE = 64

# player settings
player_settings = {
    'position': (WIDTH//2, HEIGHT//2),
    'angle': 0,
    'speed': 1.3
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

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
GRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
GOLDENROD_LIGHT = (153, 114, 15)
GOLDENROD = (71, 53, 7)
