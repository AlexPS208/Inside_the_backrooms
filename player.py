import pygame
from math import sin, cos
from settings import *


class Player:
    def __init__(self):
        self.x, self.y = player_settings['position']
        self.angle = player_settings['angle']

    @property
    def pos(self):
        return (self.x, self.y)

    def move(self):
        sin_a = sin(self.angle)
        cos_a = cos(self.angle)

        keys = pygame.key.get_pressed()
        # Press W
        if keys[pygame.K_w]:
            self.x += player_settings['speed'] * cos_a
            self.y += player_settings['speed'] * sin_a
        # Press S
        if keys[pygame.K_s]:
            self.x += (-player_settings['speed']+0.3) * cos_a
            self.y += (-player_settings['speed']+0.3) * sin_a
        # Press A
        if keys[pygame.K_a]:
            self.x += (player_settings['speed']-0.3) * sin_a
            self.y += (-player_settings['speed']+0.3) * cos_a
        # Press D
        if keys[pygame.K_d]:
            self.x += (-player_settings['speed']+0.3) * sin_a
            self.y += (player_settings['speed']-0.3) * cos_a
        # Press LEFT
        if keys[pygame.K_LEFT]:
            self.angle -= player_settings['speed']/90
        # Press RIGHT
        if keys[pygame.K_RIGHT]:
            self.angle += player_settings['speed']/90
