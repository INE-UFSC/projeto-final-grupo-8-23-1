import pygame


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
