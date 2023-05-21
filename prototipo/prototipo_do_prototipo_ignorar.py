import pygame
import sys


class Sistema:
    def __init__(self, lista):
        self.entidades = lista

    def adicionar_entidade(self, entidade):
        self.entidades.append(entidade)

    def remover_entidade(self, entidade):
        self.entidades.remove(entidade)

    def get_entidades(self):
        return self.entidades

    def tick():
        pass


class SistemaInimigos(Sistema):
    def __init__(self, inimigos, player):
        self.player = player
        super().__init__(inimigos)

    def tick(self):
        self.removed = []
        for enemy in self.entidades:
            enemy.rect.x += enemy.direction
            if enemy.rect.x + enemy.rect.width >= 800 or enemy.rect.x <= 0:
                enemy.direction *= -1
            if self.player.rect.colliderect(enemy.rect) and self.player.is_jumping:
                self.removed.append(enemy)
                self.remover_entidade(enemy)
            elif self.player.rect.colliderect(enemy.rect) and not \
                    self.player.is_jumping and not self.player.is_invincible:
                self.player.lives -= 1
                self.player.is_invincible = True
                self.player.invincible_ticks = pygame.time.get_ticks()

    def check_removed(self):
        return self.removed


class SistemaGravidade(Sistema):
    def __init__(self, lista, plataformas):
        self.__plataformas = plataformas
        self.gravidade = 1
        super().__init__(lista)

    def tick(self):
        for entidade in self.entidades:
            if entidade.is_jumping:
                entidade.rect.y += entidade.velocity
                entidade.velocity += self.gravidade
                for plataforma in self.__plataformas:
                    if entidade.rect.colliderect(plataforma):
                        entidade.is_jumping = False
                        entidade.rect.y = 450
                        entidade.velocity = 0
                        break


class SistemaDesenho(Sistema):
    def __init__(self, lista_sistemas, player, screen):
        self.__screen = screen
        self.__lista = []
        for lista in lista_sistemas:
            for entidade in lista.get_entidades():
                self.__lista.append(entidade)
        self.__lista.append(player)

        super().__init__(self.__lista)

    def tick(self):
        for entidade in self.__lista:
            self.__screen.blit(entidade.image, entidade.rect)


class SistemaPlataformas(Sistema):
    def __init__(self, lista):
        super().__init__(lista)

    def tick(self):
        pass


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.enemies = [Enemy(300, 500)]
        self.platform = Platform()
        self.font = pygame.font.Font(None, 36)
        self.start_ticks = pygame.time.get_ticks()
        self.hud = Hud(self)
        self.inicializar_sistemas()

    def inicializar_sistemas(self):
        self.sistemas = []
        self.inimigos = SistemaInimigos([Enemy(300, 500)], self.player)
        self.sistemas.append(self.inimigos)

        gravidade = SistemaGravidade([self.player], [self.platform])
        self.sistemas.append(gravidade)

        plataformas = SistemaPlataformas([self.platform])
        self.sistemas.append(plataformas)

        desenho = SistemaDesenho([plataformas, gravidade, self.inimigos], self.player, self.screen)
        self.sistemas.append(desenho)

    def rodar_sistemas(self):
        for sistema in self.sistemas:
            sistema.tick()
        list_removed = self.inimigos.check_removed()
        for removed in list_removed:
            for sistema in self.sistemas:
                if removed in sistema.get_entidades():
                    sistema.remover_entidade(removed)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.player.update()
            self.rodar_sistemas()

            if self.player.lives <= 0:
                print("O tyska te pegou!")
                pygame.quit()
                sys.exit()

            self.hud.update()  # Update the HUD

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


if __name__ == "__main__":
    game = Game()
    game.run()
