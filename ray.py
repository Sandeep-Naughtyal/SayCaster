import math
from map import TILESIZE

def cast_ray(px, py, angle, game_map, max_depth=500):
    step_size = 1  # smaller = more precise, but slower
    ray_x = px
    ray_y = py

    sin_a = math.sin(angle)
    cos_a = math.cos(angle)

    for depth in range(max_depth):
        ray_x += cos_a * step_size
        ray_y += sin_a * step_size

        grid_x = int(ray_x // TILESIZE)
        grid_y = int(ray_y // TILESIZE)

        # Out of bounds check
        if grid_y >= game_map.rows or grid_x >= game_map.cols or grid_y < 0 or grid_x < 0:
            break

        # Hit wall
        if game_map.grid[grid_y][grid_x] == 1:
            return math.sqrt((ray_x - px)**2 + (ray_y - py)**2), ray_x, ray_y

    return max_depth, ray_x, ray_y  # No hit
