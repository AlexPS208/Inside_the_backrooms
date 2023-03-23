import pygame
from settings import *
from player import Player
from drawing import Drawing

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

    # Tickrait
    pygame.display.flip()
    clock.tick(FPS)
