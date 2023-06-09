import pygame
import random


class Entity:
    def __init__(self, width, height, x, y, color):
        self.height = height
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0


class Player(Entity):
    def __init__(self):
        super().__init__(50, 50, 500, 450, (255, 255, 255))
        self.velocity = 0
        self.is_jumping = False
        self.is_invincible = False
        self.invincible_ticks = 0
        self.lives = 3
        self.acceleration = 1

    def jump(self):
        self.velocity = -15
        self.is_jumping = True


class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(50, 50, x, y, (255, 0, 0))
        self.acceleration = 1
        self.is_jumping = False
        self.velocity = 0
        self.direction = [random.choice([-2, 2]), random.choice([-2, 2])]

class Platform(Entity):
    def __init__(self):
        super().__init__(800, 50, 0, 550, (0, 255, 0))
