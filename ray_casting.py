import pygame
from math import sin, cos
from settings import *
from map import world_map


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def projection_color(depth):
    hex = 255 / (1+depth**2*0.0001)
    return (hex, hex // 2, 0)


def gradient_rect(window, left_colour, right_colour, target_rect):
    """ Draw a vertical-gradient filled rectangle covering <target_rect> """

    colour_rect = pygame.Surface((2, 2))
    pygame.draw.line(colour_rect, left_colour,  (0, 0), (1, 0))
    pygame.draw.line(colour_rect, right_colour, (1, 1), (0, 1))
    colour_rect = pygame.transform.smoothscale(
        colour_rect, (target_rect.width, target_rect.height))
    window.blit(colour_rect, target_rect)


def ray_casting(screen, player_pos, player_angle):
    """ Draw a map walls, which colors depends from depth between player and wall. Need player's position as (x, y) and player's angle of seen"""

    # Start datas
    x0, y0 = player_pos
    xm, ym = mapping(x0, y0)
    current_angle = player_angle - HALF_FOV

    # Ray loop
    for ray in range(NUM_RAYS):
        sin_a = sin(current_angle)
        cos_a = cos(current_angle)

        # Verticals checking
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for vertical in range(0, WIDTH, TILE):
            depth_v = (x-x0) / cos_a
            y = y0 + depth_v*sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE

        # Horizontal checking
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for horizontal in range(0, WIDTH, TILE):
            depth_h = (y-y0) / sin_a
            x = x0 + depth_h*cos_a
            if mapping(x, y+dy) in world_map:
                break
            y += dy * TILE

        # Depth metering
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= cos(player_angle - current_angle)
        if depth == 0:
            # Next ray
            current_angle += DELTA_ANGLE
            continue

        # Projection's datas
        proj_height = PROJ_COEF/depth
        color = projection_color(depth)
        coords = (ray*SCALE, HEIGHT/2 -
                  proj_height//2, SCALE, proj_height)

        # Projection
        pygame.draw.rect(screen, color, coords)
        # Next ray
        current_angle += DELTA_ANGLE
