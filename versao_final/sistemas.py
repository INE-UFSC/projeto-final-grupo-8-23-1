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


class SistemaInimigosShooter(Sistema):
    def __init__(self, inimigos, player):
        self.player = player
        super().__init__(inimigos)

    def tick(self):
        self.removed = []
        for enemy in self.entidades:
            enemy.rect.x += enemy.direction[0]
            enemy.rect.y += enemy.direction[1]
            if self.player.rect.colliderect(enemy.rect) and pygame.key.get_pressed()[pygame.K_SPACE]:
                self.removed.append(enemy)
                self.remover_entidade(enemy)

            if enemy.rect.x + enemy.rect.width >= 1200 or enemy.rect.x <= 0:
                enemy.direction[0] *= -1
            if enemy.rect.y + enemy.rect.height >= 650 or enemy.rect.y <= 70:
                enemy.direction[1] *= -1

    def check_removed(self):
        return self.removed


class SistemaInimigosFlappy(Sistema):
    def __init__(self, inimigos, player):
        self.player = player
        super().__init__(inimigos)

    def tick(self):
        self.removed = []
        for enemy in self.entidades:
            if self.player.rect.colliderect(enemy.rect):
                self.removed.append(enemy)
                self.remover_entidade(enemy)
    def check_removed(self):
        return self.removed


class SistemaInimigosMario(Sistema):
    def __init__(self, inimigos, player):
        self.player = player
        super().__init__(inimigos)
        self.removed = []

    def tick(self):
        for enemy in self.entidades:
            enemy.rect.x += enemy.direction[0]
            if enemy.rect.x + enemy.rect.width >= 1200 or enemy.rect.x <= 0:
                enemy.direction[0] *= -1
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


class SistemaMovimento(Sistema):
    def __init__(self, listas, player):
        self.__lista = []
        self.__lista.append(player)
        for lista in listas:
            for entidade in lista.get_entidades():
                self.__lista.append(entidade)
        super().__init__(self.__lista)

    def tick(self):
        for entidade in self.entidades:
            entidade.rect.x += entidade.vel_x
            entidade.rect.y += entidade.vel_y
            if entidade.vel_x > 0:
                entidade.vel_x = max(0, entidade.vel_x - entidade.acceleration)
            elif entidade.vel_x < 0:
                entidade.vel_x = min(0, entidade.vel_x + entidade.acceleration)


class SistemaGravidade(Sistema):
    def __init__(self, player, plataformas, inimigos, gravidade):
        self.__plataformas = plataformas
        self.gravidade = gravidade
        self.__lista = inimigos.copy()
        self.__lista.append(player)
        super().__init__(self.__lista)

    def tick(self):
        for entidade in self.entidades:
            entidade.rect.y += entidade.velocity
            entidade.velocity += self.gravidade
            for plataforma in self.__plataformas:
                if entidade.rect.colliderect(plataforma):
                    entidade.is_jumping = False
                    entidade.rect.y = plataforma.rect.y - entidade.height
                    entidade.velocity = 0
                    break

class SistemaTrocaLado(Sistema):
    def __init__(self, player):
        super().__init__([player])

    def tick(self):
        for player in self.entidades:
            if player.rect.x < 0:
                player.rect.x = 1200
            elif player.rect.x > 1200:
                player.rect.x = 0


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

class PlayerFlappySistema(Sistema):
    def __init__(self, player):
        super().__init__([player])

    def tick(self):
        for player in self.entidades:
            player.vel_x = 4
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                player.jump_flappy()

            if player.rect.y >= 599:
                player.lives -= 1
                player.rect.y = 250



class PlayerShooterSistema(Sistema):
    def __init__(self, player):
        super().__init__([player])

    def tick(self):
        for player in self.entidades:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player.rect.x -= 5
            if keys[pygame.K_d]:
                player.rect.x += 5
            if keys[pygame.K_w]:
                player.rect.y -= 5
            if keys[pygame.K_s]:
                player.rect.y += 5


class PlayerMarioSistema(Sistema):
    def __init__(self, player):
        super().__init__([player])

    def tick(self):
        for player in self.entidades:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player.vel_x = -5
            if keys[pygame.K_d]:
                player.vel_x = 5
            if keys[pygame.K_SPACE] and not player.is_jumping:
                player.jump()
            if player.is_invincible:
                if pygame.time.get_ticks() - player.invincible_ticks > 1200:
                    player.is_invincible = False
