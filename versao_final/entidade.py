import pygame
import random


class Entity:
    def __init__(self, width, height, x, y, color):
        self.width = width
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
        self.tiro_pronto = True
        self.invincible_ticks = 0
        self.tempo_recarga = 300
        self.lives = 3
        self.acceleration = 1

    def get_vidas(self):
        return self.lives

    def jump(self):
        self.velocity = -16
        self.is_jumping = True

    def jump_flappy(self):
        self.velocity = -5
        self.is_jumping = True
    
    def shoot(self):
        self.tiro_pronto = False


class Enemy(Entity):
    def __init__(self, x, y, color):
        super().__init__(50, 50, x, y, color)
        self.acceleration = 1
        self.velocity = 0
        self.direction = [random.choice([-2, 2]), random.choice([-3, -2, -1, 1, 2, 3])]

class Bullet(Entity):
    def __init__(self, x, y, direction_x, direction_y):
        super().__init__(5, 5, x, y, (255, 255, 0))
        self.direction = [direction_x, direction_y]

class Platform(Entity):
    def __init__(self):
        super().__init__(1200, 50, 0, 650, (0, 255, 0))
