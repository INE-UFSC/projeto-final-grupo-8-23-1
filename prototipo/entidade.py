import pygame


class Entity:
    def __init__(self, width, height, x, y, color):
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(Entity):
    def __init__(self):
        super().__init__(50, 100, 500, 450, (255, 255, 255))
        self.velocity = 0
        self.is_jumping = False
        self.is_invincible = False
        self.invincible_ticks = 0
        self.lives = 3

    def jump(self):
        self.velocity = -15
        self.is_jumping = True

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.jump()
        if self.is_invincible:
            if pygame.time.get_ticks() - self.invincible_ticks > 1200:
                self.is_invincible = False


class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(50, 50, x, y, (255, 0, 0))
        self.direction = 2


class Platform(Entity):
    def __init__(self):
        super().__init__(800, 50, 0, 550, (0, 255, 0))
