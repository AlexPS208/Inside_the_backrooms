import pygame
from settings import *
from player import Player
from drawing import Drawing

# import for minimap
import math
from map import world_map

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Inside the Backrooms')
icon = pygame.image.load('./src/icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
render = Drawing(screen)

player = Player()

while True:
    # Close game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Player control
    player.move()

    # Render
    render.background()
    render.world(player.pos, player.angle)
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
