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
        self.removed = []
        super().__init__(inimigos)

    def check_removed(self):
        return self.removed


class SistemaInimigosShooter(SistemaInimigos):
    def tick(self):
        self.removed = []
        for enemy in self.entidades:
            enemy.rect.x += enemy.direction[0]
            enemy.rect.y += enemy.direction[1]

            entidades_sem_1 = self.entidades.copy()
            entidades_sem_1.remove(enemy)
            for enemy_2 in entidades_sem_1:
                if enemy.rect.colliderect(enemy_2.rect):
                    enemy_2.direction[0] *= -1
                    enemy_2.direction[1] *= -1

            if self.player.rect.colliderect(enemy.rect) and pygame.key.get_pressed()[pygame.K_SPACE]:
                self.removed.append(enemy)
                self.remover_entidade(enemy)

            if enemy.rect.x + enemy.rect.width > 1200 or enemy.rect.x < 0:
                enemy.direction[0] *= -1
            if enemy.rect.y + enemy.rect.height > 650 or enemy.rect.y < 70:
                enemy.direction[1] *= -1


class SistemaInimigosAsteroid(SistemaInimigos):
    def tick(self):
        self.removed = []
        for enemy in self.entidades:
            enemy.rect.x += enemy.direction[0]
            enemy.rect.y += enemy.direction[1]

            entidades_sem_1 = self.entidades.copy()
            entidades_sem_1.remove(enemy)
            for enemy_2 in entidades_sem_1:
                if enemy.rect.colliderect(enemy_2.rect):
                    enemy_2.direction[0] *= -1
                    enemy_2.direction[1] *= -1

            if self.player.rect.colliderect(enemy.rect) and pygame.key.get_pressed()[pygame.K_SPACE]:
                self.removed.append(enemy)
                self.remover_entidade(enemy)

            if enemy.rect.x + enemy.rect.width > 1200 or enemy.rect.x < 0:
                enemy.direction[0] *= -1
            if enemy.rect.y + enemy.rect.height > 650 or enemy.rect.y < 70:
                enemy.direction[1] *= -1


class SistemaInimigosFlappy(SistemaInimigos):
    def tick(self):
        self.removed = []
        for enemy in self.entidades:
            if self.player.rect.colliderect(enemy.rect):
                self.removed.append(enemy)
                self.remover_entidade(enemy)


class SistemaInimigosMario(SistemaInimigos):
    def tick(self):
        for enemy in self.entidades:
            enemy.rect.x += enemy.direction[0]

            entidades_sem_1 = self.entidades.copy()
            entidades_sem_1.remove(enemy)
            for enemy_2 in entidades_sem_1:
                if enemy.rect.colliderect(enemy_2.rect):
                    if enemy.rect.y == enemy_2.rect.y:
                        enemy_2.direction[0] *= -1
                    elif enemy.rect.y > enemy_2.rect.y:
                        enemy_2.velocity = -10
            if enemy.rect.x + enemy.rect.width > 1200 or enemy.rect.x < 0:
                enemy.direction[0] *= -1
            if self.player.rect.colliderect(enemy.rect) and self.player.is_jumping:
                self.player.jump()
                self.removed.append(enemy)
                self.remover_entidade(enemy)
            elif self.player.rect.colliderect(enemy.rect) and not \
                    self.player.is_jumping and not self.player.is_invincible:
                self.player.lives -= 1
                self.player.is_invincible = True
                self.player.invincible_ticks = pygame.time.get_ticks()


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


class SistemaPlayer(Sistema):
    def __init__(self, player):
        self.player = player
        super().__init__([player])


class SistemaPlayerTrocaLadoHorizontal(SistemaPlayer):
    def tick(self):
        if self.player.rect.x < - (self.player.width/2):
            self.player.rect.x = 1200 - (self.player.width/2)
        elif self.player.rect.x > 1200 - (self.player.width/2):
            self.player.rect.x = - (self.player.width/2)


class SistemaPlayerTrocaLadoVertical(SistemaPlayer):
    def tick(self):
        if self.player.rect.y < 65:  # altura da hud
            self.player.rect.y = 650 - self.player.height
        elif self.player.rect.y > (650 - self.player.height):  # altura plataforma
            self.player.rect.y = 65


class SistemaPlayerBateParedeHorizontal(SistemaPlayer):
    def tick(self):
        if self.player.rect.x < 0:
            self.player.rect.x = 0
        elif self.player.rect.x > 1200 - self.player.width:
            self.player.rect.x = 1200 - self.player.width


class SistemaPlayerBateParedeVertical(SistemaPlayer):
    def tick(self):
        if self.player.rect.y < 65:
            self.player.rect.y = 65
        elif self.player.rect.y > (650 - self.player.height):
            self.player.rect.y = 650 - self.player.height


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


class PlayerFlappySistema(SistemaPlayer):
    def tick(self):
        self.player.vel_x = 3.5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player.jump_flappy()

        if self.player.rect.y > 599:
            self.player.lives -= 1
            self.player.rect.y = 200
            self.player.vel_y = 0


class PlayerShooterSistema(SistemaPlayer):
    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.rect.x -= 5
        if keys[pygame.K_d]:
            self.player.rect.x += 5
        if keys[pygame.K_w]:
            self.player.rect.y -= 5
        if keys[pygame.K_s]:
            self.player.rect.y += 5


class PlayerMarioSistema(SistemaPlayer):
    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.vel_x = -5
        if keys[pygame.K_d]:
            self.player.vel_x = 5
        if keys[pygame.K_SPACE] and not self.player.is_jumping:
            self.player.jump()
        if self.player.is_invincible:
            if pygame.time.get_ticks() - self.player.invincible_ticks > 1200:
                self.player.is_invincible = False


class PlayerAsteroidSistema(SistemaPlayer):
    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.rect.x -= 5
        if keys[pygame.K_d]:
            self.player.rect.x += 5
        if keys[pygame.K_w]:
            self.player.rect.y -= 5
        if keys[pygame.K_s]:
            self.player.rect.y += 5
        if keys[pygame.K_SPACE] and self.player.tiro_pronto:
            ultimo_tiro = pygame.time.get_ticks()
            self.player.shoot()
        if not self.player.tiro_pronto:
            if pygame.time.get_ticks() - ultimo_tiro > self.player.tempo_recarga:
                self.player.tiro_pronto = True
