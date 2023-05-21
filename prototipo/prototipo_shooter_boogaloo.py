import pygame
import sys
import random
from sistemas import SistemaDesenho, SistemaInimigos, SistemaGravidade,\
        SistemaPlataformas
from jogoabstrato import JogoAbstrato


class Shooter(JogoAbstrato):
    def __init__(self, entidades=[]):
        super().__init__(entidades)

    def inicializar_entidades(self, entidades=[]):
        self.player = Player()
        self.enemies = [Enemy(random.randint(0, 750), random.randint(0, 500))
                        for _ in range(4)]
        self.platform = [Platform()]

        self.entidades.append(self.player)
        for inimigo in self.enemies:
            self.entidades.append(inimigo)
        for plataforma in self.platform:
            self.entidades.append(plataforma)

    def inicializar_sistemas(self):
        self.sistemas = []
        self.inimigos = SistemaInimigos(self.enemies, self.player)
        self.sistemas.append(self.inimigos)

        gravidade = SistemaGravidade([self.player], self.platform)
        self.sistemas.append(gravidade)

        plataformas = SistemaPlataformas(self.platform)
        self.sistemas.append(plataformas)

        desenho = SistemaDesenho([plataformas, gravidade, self.inimigos], self.player, self.screen)
        self.sistemas.append(desenho)


class Entity:
    def __init__(self, game, width, height, x, y, color):
        self.game = game
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.game.screen.blit(self.image, self.rect)


class Player(Entity):
    def __init__(self, game):
        super().__init__(game, 50, 100, 500, 450, (255, 255, 255))
        self.is_invincible = False
        self.lives = 3

    def update(self):
        super().update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5


class Enemy(Entity):
    def __init__(self, game, x, y):
        super().__init__(game, 50, 50, x, y, (255, 0, 0))
        self.direction = [random.uniform(-2, 2), random.uniform(-2, 2)]
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        super().update()
