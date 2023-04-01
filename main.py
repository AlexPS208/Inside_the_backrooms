import pygame
from settings import *
from player import Player
from drawing import Drawing
from map_gen import map_comparing, map_parts_generate, wall_coordinates

# import for minimap
import math

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Inside the Backrooms')
icon = pygame.image.load('./src/icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
render = Drawing(screen)

player = Player()

text_map, map_parts = map_comparing(map_parts_generate())
world_map, collision_walls = wall_coordinates(text_map)


while True:
    # Close game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Player control
    player.movement(world_map)

    # Render
    render.background()

    text_map, map_parts = player.escape_room(text_map, map_parts)
    world_map, collision_walls = wall_coordinates(text_map)
    render.world(player.pos, player.angle, world_map)
    render.fps(clock)

    # mini-map (вырезать потом)
    pygame.draw.line(screen, RED, (player.x//15, player.y//15), (player.x//15 + 10 *
                     math.cos(player.angle), player.y//15 + 10 * math.sin(player.angle)), 1)
    pygame.draw.circle(
        screen, GREEN, (int(player.x//15), int(player.y//15)), 3)
    for x, y in world_map:
        pygame.draw.rect(screen, GRAY, (x//15, y//15, TILE//15, TILE//15), 2)

    # Tickrait
    pygame.display.flip()
    clock.tick(FPS)
