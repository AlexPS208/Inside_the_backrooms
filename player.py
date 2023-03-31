import pygame
from math import sin, cos
from settings import *
from map_gen import up_shift, down_shift, left_shift, right_shift


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

    def escape_room(self, world_map, map_parts):
        room_up, room_left = MAP_SIZE*TILE, MAP_SIZE*TILE-TILE
        room_down, room_right = MAP_SIZE*2*TILE, MAP_SIZE*2*TILE-TILE*2

        # Going room up
        if self.y < room_up:
            self.y = room_down-1
            world_map, map_parts = up_shift(map_parts)
        # Going room down
        if self.y > room_down:
            self.y = room_up+1
            world_map, map_parts = down_shift(map_parts)
        # Going room left
        if self.x < room_left:
            self.x = room_right-1
            world_map, map_parts = left_shift(map_parts)
        # Going room right
        if self.x > room_right:
            self.x = room_left+1
            world_map, map_parts = right_shift(map_parts)

        return (world_map, map_parts)
