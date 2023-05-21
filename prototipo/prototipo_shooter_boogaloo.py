import pygame
import sys
import random


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.player = Player(self)
        self.enemies = [Enemy(self, random.randint(0, 750), random.randint(0, 500)) for _ in range(4)]
        self.platform = Platform(self)
        self.font = pygame.font.Font(None, 36)
        self.start_ticks = pygame.time.get_ticks()
        self.hud = Hud(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))

            self.player.update()
            self.platform.update()

            for enemy in self.enemies:
                enemy.update()
                if self.player.rect.colliderect(enemy.rect) and pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.enemies.remove(enemy)
                #elif not self.player.is_invincible:
                    #if pygame.time.get_ticks() % 9000 <= 10:
                        #self.player.lives -= 1
                        #self.enemies.remove(enemy)

            if self.player.lives <= 0:
                print("O tyska te pegou!")
                pygame.quit()
                sys.exit()

            self.hud.update()

            pygame.display.flip()
            self.clock.tick(90)


class Hud:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 36)
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000
        timer_text = self.font.render("Tempo: " + str(seconds), True, (255, 255, 255))
        self.game.screen.blit(timer_text, (620, 10))

        lives_text = self.font.render("Vidas: ", True, (255, 255, 255))
        self.game.screen.blit(lives_text, (20, 10))

        lives_text = self.font.render(str(self.game.player.lives), True, (255, 0, 0))
        self.game.screen.blit(lives_text, (100, 10))




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
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

        if self.rect.x + self.rect.width >= 800 or self.rect.x <= 0:
            self.direction[0] *= -1
        if self.rect.y + self.rect.height >= 550 or self.rect.y <= 0:
            self.direction[1] *= -1


class Platform(Entity):
    def __init__(self, game):
        super().__init__(game, 800, 50, 0, 550, (0, 255, 0))


game = Game()
game.run()
