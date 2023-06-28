import pygame
import random
import math


#---------------------------------------------------INICIALIZAÇÃO---------------------------------------------------#


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
        self.multiplier = 1.5
        self.velocity = 0
        self.is_jumping = False
        self.is_invincible = True
        self.tiro_pronto = 0
        self.invincible_ticks = 0
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

    def update(self):
        self.current_sprite += 0.1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]


class Enemy(Entity):
    def __init__(self, x, y, color, multiplier, x_sprite, y_sprite):
        self.multiplier = multiplier
        self.x_sprite = x_sprite
        self.y_sprite = y_sprite
        self.scale = (self.x_sprite * self.multiplier, self.y_sprite * self.multiplier)
        self.acceleration = 1
        self.velocity = 0
        self.is_running = True
        self.direction = [random.choice([-2, 2]), random.choice([-3, -2, -1, 1, 2, 3])]
        super().__init__(self.scale[0], self.scale[1], x, y, color)

    def update(self):
        self.current_sprite += 0.1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]


#---------------------------------------------------ASTEROID---------------------------------------------------#


class PlayerAsteroid(Player):
    def load_animation(self):
        self.multiplier = 1.5
        scale = (28 * self.multiplier, 30 * self.multiplier)
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_bola_1.png'), (scale[0], scale[1])))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_bola_2.png'), (scale[0], scale[1])))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_bola_3.png'), (scale[0], scale[1])))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_bola_4.png'), (scale[0], scale[1])))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]

class InimigoAsteroid(Enemy):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 2, 25, 21)

    def load_animation(self):
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_laranja_voando_1.png'), self.scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_laranja_voando_2.png'), self.scale))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]


#---------------------------------------------------DINO---------------------------------------------------#


class PlayerDino(Player):
    def load_animation(self):
        scale = (27 * self.multiplier, 40 * self.multiplier)
        self.sprite_pulando = pygame.transform.scale(pygame.image.load('./assets/player/mario_pulando.png'), scale)
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_1.png'), scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_2.png'), scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_3.png'), scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_4.png'), scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_5.png'), scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_6.png'), scale))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]

    def update(self):
        if self.is_jumping:
            self.image = self.sprite_pulando
        else:
            self.current_sprite += 0.1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]


class DinoEnemy(Enemy):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 2.5, 17, 21)

    def load_animation(self):
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_azul_andando_1.png'), self.scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_azul_andando_2.png'), self.scale))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]


#---------------------------------------------------FLAPPY---------------------------------------------------#


class PlayerFlappy(Player):
    def load_animation(self):
        scale = (40 * self.multiplier, 29 * self.multiplier)
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_flappy.png'), (scale[0], scale[1])))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]


class InimigoFlappy(Enemy):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 2, 25, 21)

    def load_animation(self):
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_verde_voando_1.png'), self.scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_verde_voando_2.png'), self.scale))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]


#---------------------------------------------------MARIO---------------------------------------------------#


class PlayerMario(Player):
    def load_animation(self):
        scale = (26 * self.multiplier, 40 * self.multiplier)
        self.sprite_parado = pygame.transform.scale(pygame.image.load('./assets/player/mario_parado.png'), scale)
        self.sprite_pulando = pygame.transform.scale(pygame.image.load('./assets/player/mario_pulando.png'), scale)
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_1.png'), scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_2.png'), scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_3.png'), scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_4.png'), scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_5.png'), scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_andando_6.png'), scale))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]

    def update(self):
        if self.is_jumping:
            self.image = self.sprite_pulando
        elif self.is_running:
            self.current_sprite += 0.1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_running = False
            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.image = self.sprite_parado


class InimigoMario(Enemy):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 2.5, 17, 21)

    def load_animation(self):
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_azul_andando_1.png'), self.scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_azul_andando_2.png'), self.scale))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]


#---------------------------------------------------SHOOTER---------------------------------------------------#


class PlayerShooter(Player):
    def load_animation(self):
        scale = (39 * self.multiplier, 39 * self.multiplier)
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_mira_1.png'), self.scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_mira_2.png'), self.scale))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]

    def update(self):
        self.current_sprite += 0.05
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]


class InimigoShooter(Enemy):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 2, 25, 21)

    def load_animation(self):
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_verde_voando_1.png'), self.scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_verde_voando_2.png'), self.scale))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]


#---------------------------------------------------SPACE---------------------------------------------------#


class PlayerSpace(Player):
    def load_animation(self):
        scale = (44 * self.multiplier, 40 * self.multiplier)
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/player/mario_space.png'), (scale[0], scale[1])))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]


class InimigoSpace(Enemy):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 2, 25, 21)

    def load_animation(self):
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_laranja_voando_1.png'), self.scale))
        self.sprites.append(pygame.transform.scale(pygame.image.load('./assets/gumbas/gumba_laranja_voando_2.png'), self.scale))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.rect.x, self.rect.y]


#---------------------------------------------------OUTROS---------------------------------------------------#


class Bullet(Entity):
    def __init__(self, x, y):
        super().__init__(5, 5, x, y, (255, 255, 0))
        self.speed = 7
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        self.angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))


class Platform(Entity, pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y, (0, 255, 0))
