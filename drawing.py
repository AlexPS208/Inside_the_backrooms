import pygame
from settings import *
from ray_casting import ray_casting, gradient_rect


class Drawing:
    def __init__(self, screen):
        self.sc = screen
        self.font = pygame.font.SysFont('Arial', 18, bold=True)

    def background(self):
        ceil_rect = pygame.Rect(0, 0, WIDTH, HEIGHT/2)
        floor_rect = pygame.Rect(0, HEIGHT/2, WIDTH, HEIGHT/2)

        gradient_rect(self.sc, GOLDENROD, BLACK, ceil_rect)
        gradient_rect(self.sc, BLACK, GOLDENROD_LIGHT, floor_rect)

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle)

    def fps(self, clock):
        display_fps = "fps: " + str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, WHITE)
        self.sc.blit(render, FPS_POS)
