import pygame
import math

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_w, K_a, K_s, K_d
)

from map import Map,TILESIZE
from ray import cast_ray

class Player:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 0.1 
        self.angle=0.1

    def move(self,dt, map):  
        keys = pygame.key.get_pressed()
        rotation_speed = 1 #IMPORTANT FOR CONTROLSSS
        move_speed=100
        # Rotates 
        if keys[K_a] or keys[K_LEFT]:
            self.angle -= rotation_speed*0.1
            if self.angle < 0:
                self.angle += 2 * math.pi
        if keys[K_d] or keys[K_RIGHT]:
            self.angle += rotation_speed*0.1
            if self.angle > 2 * math.pi:
                self.angle -= 2 * math.pi

        # Direction vector based on angle (maths)
        dx = math.cos(self.angle) * move_speed*dt
        dy = math.sin(self.angle) * move_speed*dt

        # Forward/backward movement 
        new_x, new_y = self.x, self.y

        if keys[K_w] or keys[K_UP]:
            new_x += dx
            new_y += dy
        if keys[K_s] or keys[K_DOWN]:
            new_x -= dx
            new_y -= dy

        # Collision detection against the map
        grid_x = int(new_x // TILESIZE)
        grid_y = int(new_y // TILESIZE)
        if map.grid[grid_y][grid_x] == 0:
            self.x = new_x
            self.y = new_y




    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.radius) # pygame.draw.circle(surface, color, center, radius)*/
        line_length = 20
        end_x = self.x + math.cos(self.angle) * line_length
        end_y = self.y + math.sin(self.angle) * line_length
        pygame.draw.line(surface, (255, 0, 0), (self.x, self.y), (end_x, end_y), 2)

    

#Main code actually starts from here, above was class and fun 
pygame.init()
SW=640
SH=480
FOV = math.pi / 3        # 60 degrees field of view
NUM_RAYS = 120           # Number of rays to cast
STEP_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 500
screen=pygame.display.set_mode((SW, SH))
pygame.display.set_caption("SayCaster")

player=Player(1 * TILESIZE + TILESIZE // 2, 1 * TILESIZE + TILESIZE // 2, 4)  # Centers the player and keeps at a cell which isnt wall
clock = pygame.time.Clock()
g_map=Map()

running= True
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
    player.move(dt,g_map)
    screen.fill((0, 0, 0))

    start_angle = player.angle - FOV / 2

    for ray in range(NUM_RAYS):
        ray_angle = start_angle + ray * STEP_ANGLE
        distance, hit_x, hit_y = cast_ray(player.x, player.y, ray_angle, g_map)

        # Fisheye correction
        corrected_distance = distance * math.cos(ray_angle - player.angle)

        # Wall height projection formula
        wall_height = (TILESIZE * 277) / (corrected_distance + 0.0001)

        # Shade based on distance (darker for farther walls)
        base_color = (200, 30, 30)  #reddish walls

        # Shading based on distance
        fog_strength = int(min(180, corrected_distance))  # Cap max fog value
        r = max(0, base_color[0] - fog_strength)
        g = max(0, base_color[1] - fog_strength)
        b = max(0, base_color[2] - fog_strength)

        color = (r, g, b)

        # Draw vertical slice
        x = int(ray * (640 / NUM_RAYS))  # width of screen
        pygame.draw.rect(screen, color, (x, 480 / 2 - wall_height / 2, 1, wall_height))


    # Cast single ray in player's direction
    distance, hit_x, hit_y = cast_ray(player.x, player.y, player.angle, g_map)



    # Mini-map 
    scale = 0.25
    offset_x, offset_y = 10, 10
    mini_width = int(g_map.cols * TILESIZE * scale)
    mini_height = int(g_map.rows * TILESIZE * scale)
    pygame.draw.rect(screen, (0, 0, 0), (offset_x, offset_y, mini_width, mini_height))

    g_map.draw(screen, scale=scale, offset_x=offset_x, offset_y=offset_y)

    # Draw mini player on minimap
    pygame.draw.circle(
        screen,
        (255, 255, 255),
        (int(offset_x + player.x * scale), int(offset_y + player.y * scale)),
        int(player.radius * scale)
    )

    # Draw direction line 
    line_length = 20 * scale
    end_x = offset_x + player.x * scale + math.cos(player.angle) * line_length
    end_y = offset_y + player.y * scale + math.sin(player.angle) * line_length
    pygame.draw.line(screen, (255, 0, 0), (offset_x + player.x * scale, offset_y + player.y * scale), (end_x, end_y), 1)

    pygame.display.flip()
   

