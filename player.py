import pygame
from math import sin, cos
from settings import *
from map_gen import up_shift, down_shift, left_shift, right_shift
from ray_casting import mapping


class Player:
    def __init__(self):
        self.x, self.y = player_settings['position']
        self.angle = player_settings['angle']
        # mouse control
        self.sensitivity = player_settings['sensitivity']
        # collision
        self.side = player_settings['side']

    @property
    def pos(self):
        return (self.x, self.y)

    def check_collision(self, dx, dy, world_map):
        if dx != 0:
            delta_x = (self.side // 2) * abs(dx) / dx
            if mapping(self.x + dx + delta_x, self.y + delta_x) in world_map:
                dx = 0
            if mapping(self.x + dx + delta_x, self.y - delta_x) in world_map:
                dx = 0
        if dy != 0:
            delta_y = (self.side // 2) * abs(dy) / dy
            if mapping(self.x + delta_y, self.y + dy + delta_y) in world_map:
                dy = 0
            if mapping(self.x - delta_y, self.y + dy + delta_y) in world_map:
                dy = 0
        self.x += dx
        self.y += dy

    def keys_control(self, world_map):
        sin_a = sin(self.angle)
        cos_a = cos(self.angle)

        keys = pygame.key.get_pressed()
        # Press W
        if keys[pygame.K_w]:
            dx = player_settings['speed'] * cos_a
            dy = player_settings['speed'] * sin_a
            self.check_collision(dx, dy, world_map)
        # Press S
        if keys[pygame.K_s]:
            dx = (-player_settings['speed']+0.3) * cos_a
            dy = (-player_settings['speed']+0.3) * sin_a
            self.check_collision(dx, dy, world_map)
        # Press A
        if keys[pygame.K_a]:
            dx = (player_settings['speed']-0.3) * sin_a
            dy = (-player_settings['speed']+0.3) * cos_a
            self.check_collision(dx, dy, world_map)
        # Press D
        if keys[pygame.K_d]:
            dx = (-player_settings['speed']+0.3) * sin_a
            dy = (player_settings['speed']-0.3) * cos_a
            self.check_collision(dx, dy, world_map)
        # Press LEFT
        if keys[pygame.K_LEFT]:
            self.angle -= player_settings['speed']/90
        # Press RIGHT
        if keys[pygame.K_RIGHT]:
            self.angle += player_settings['speed']/90

    # def mouse_control(self):
    #     if pygame.mouse.get_focused():
    #         difference = pygame.mouse.get_pos()[0] - WIDTH//2
    #         pygame.mouse.set_pos((WIDTH//2, HEIGHT//2))
    #         self.angle += difference * self.sensitivity

    def movement(self, world_map):
        self.keys_control(world_map)
        # self.mouse_control()
        self.angle %= DOUBLE_PI

    def escape_room(self, world_map, map_parts):
        # Going room up
        if self.y < ROOM_UP:
            self.y = ROOM_DOWN-1
            world_map, map_parts = up_shift(map_parts)
        # Going room down
        if self.y > ROOM_DOWN:
            self.y = ROOM_UP+1
            world_map, map_parts = down_shift(map_parts)
        # Going room left
        if self.x < ROOM_LEFT:
            self.x = ROOM_RIGHT-1
            world_map, map_parts = left_shift(map_parts)
        # Going room right
        if self.x > ROOM_RIGHT:
            self.x = ROOM_LEFT+1
            world_map, map_parts = right_shift(map_parts)

        return (world_map, map_parts)
