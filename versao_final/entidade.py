import pygame
import random


class Entity:
    def __init__(self, width, height, x, y, color):
        self.color = color
        self.width = width
        self.height = height
        self.sprites = []
        self.load_animation()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0

    def load_animation(self):
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def update(self):
        pass


class Player(Entity, pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        self.velocity = 0
        self.is_jumping = False
        self.is_invincible = True
        self.tiro_pronto = True
        self.ultimo_tiro = 0
        self.invincible_ticks = 0
        self.tempo_recarga = 300
        self.lives = 3
        self.acceleration = 1
        self.is_running = False
        super().__init__(width, height, x, y, (255, 255, 255))

    def animate_run(self):
        self.is_running = True

    def get_vidas(self):
        return self.lives

    def jump(self):
        self.velocity = -16
        self.is_jumping = True

    def jump_flappy(self):
        self.velocity = -5
        self.is_jumping = True


class PlayerFlappy(Player):
    def load_animation(self):
        self.sprites.append(pygame.image.load('./assets/player/mario_flappy.png'))
        self.sprite_parado = (pygame.image.load('./assets/player/mario_flappy.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]

    def update(self):
        if self.is_running:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_running = False
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.image = self.sprite_parado


class PlayerAsteroid(Player):
    def load_animation(self):
        self.sprites.append(pygame.image.load('./assets/player/mario_bola_1.png'))
        self.sprites.append(pygame.image.load('./assets/player/mario_bola_2.png'))
        self.sprites.append(pygame.image.load('./assets/player/mario_bola_3.png'))
        self.sprite_parado = (pygame.image.load('./assets/player/mario_bola_1.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]

    def update(self):
        if self.is_running:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_running = False
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.image = self.sprite_parado


class PlayerShooter(Player):
    def load_animation(self):
        self.sprites.append(pygame.image.load('./assets/player/mario_mira_1.png'))
        self.sprite_parado = (pygame.image.load('./assets/player/mario_mira_2.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]

    def update(self):
        if self.is_running:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_running = False
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.image = self.sprite_parado


class PlayerMario(Player):
    def load_animation(self):
        self.sprite_parado = pygame.image.load('./assets/player/mario_parado.png')
        self.sprites.append(pygame.image.load('./assets/player/mario_andando_1.png'))
        self.sprites.append(pygame.image.load('./assets/player/mario_andando_2.png'))
        self.sprites.append(pygame.image.load('./assets/player/mario_andando_3.png'))
        self.sprites.append(pygame.image.load('./assets/player/mario_andando_4.png'))
        self.sprites.append(pygame.image.load('./assets/player/mario_andando_5.png'))
        self.sprites.append(pygame.image.load('./assets/player/mario_andando_6.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]

    def update(self):
        if self.is_running:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_running = False
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.image = self.sprite_parado


class Enemy(Entity):
    def __init__(self, x, y, color):
        self.acceleration = 1
        self.velocity = 0
        self.is_running = True
        self.direction = [random.choice([-2, 2]), random.choice([-3, -2, -1, 1, 2, 3])]
        super().__init__(50, 50, x, y, color)

    def update(self):
        self.current_sprite += 0.2
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_running = False
        self.image = self.sprites[int(self.current_sprite)]


class MarioEnemy(Enemy):
    def load_animation(self):
        self.sprites.append(pygame.image.load('./assets/gumbas/gumba_azul_andando_1.png'))
        self.sprites.append(pygame.image.load('./assets/gumbas/gumba_azul_andando_2.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]


class InimigoVoador(Enemy):
    def load_animation(self):
        self.sprites.append(pygame.image.load('./assets/gumbas/gumba_azul_voando_1.png'))
        self.sprites.append(pygame.image.load('./assets/gumbas/gumba_azul_voando_2.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]


class Bullet(Entity):
    def __init__(self, x, y, vel_x, vel_y):
        super().__init__(5, 5, x, y, (255, 255, 0))
        self.direction = [vel_x, vel_y]


class Platform(Entity):
    def __init__(self):
        super().__init__(1200, 50, 0, 650, (0, 255, 0))
