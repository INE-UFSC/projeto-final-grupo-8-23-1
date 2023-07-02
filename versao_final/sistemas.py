import pygame
from entidade import *

# ----INICIALIZAÇÃO---


class Sistema:
    def __init__(self, lista):
        self.entidades = lista
        self.sistemas = []

    def adicionar_sistema(self, sistema):
        self.sistemas.append(sistema)

    def adicionar_entidade(self, entidade):
        self.entidades.append(entidade)

    def remover_entidade(self, entidade):
        if entidade in self.entidades:
            self.entidades.remove(entidade)
        else:
            for sistema in self.sistemas:
                if entidade in sistema.get_entidades():
                    sistema.remover_entidade(entidade)

    def get_entidades(self):
        temp = []
        for entidade in self.entidades:
            temp.append(entidade)
        for sistema in self.sistemas:
            for entidade in sistema.get_entidades():
                temp.append(entidade)
        return temp

    def tick():
        pass


class SistemaPlayer(Sistema):
    def __init__(self, player):
        self.player = player
        super().__init__([])

    def recarga(self):
        if self.player.is_invincible:
            if pygame.time.get_ticks() - self.player.invincible_ticks > self.player.invincible_duration:
                self.player.is_invincible = False

        if self.player.tomando_dano:
            if pygame.time.get_ticks() - self.player.damage_ticks > self.player.damage_duration:
                self.player.tomando_dano = False

        if not self.player.tiro_pronto:
            if pygame.time.get_ticks() - self.player.ultimo_tiro > self.player.tiro_recarga:
                self.player.tiro_pronto = True


class SistemaInimigos(Sistema):
    def __init__(self, inimigos, player, plataformas):
        super().__init__(inimigos)
        self.player = player
        self.removed = []
        self.plataformas = plataformas

    def check_removed(self):
        return self.removed

    def clear_removed(self):
        self.removed.clear()


#---------------------------------------------------ASTEROID---------------------------------------------------#


class PlayerAsteroidSistema(SistemaPlayer):
    def tick(self):
        self.recarga()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.rect.x -= 4
            self.player.vel_x = -3
        if keys[pygame.K_d]:
            self.player.rect.x += 4
            self.player.vel_x = 3
        if keys[pygame.K_w]:
            self.player.rect.y -= 4
            self.player.vel_y = -3
        if keys[pygame.K_s]:
            self.player.rect.y += 4
            self.player.vel_y = 3
        if keys[pygame.K_SPACE]:
            self.shoot()
        if self.player.tiros_prontos > 0:
            self.player.tiros_prontos -= 1
        self.update_bullets()

    def update_bullets(self):
        for bullet in self.get_entidades():
            bullet.rect.x += bullet.vel_x
            bullet.rect.y += bullet.vel_y

    def shoot(self):
        if self.player.tiros_prontos == 0:
            bullet = Bullet(self.player.rect.x, self.player.rect.y, self.player.vel_x, self.player.vel_y)
            self.adicionar_entidade(bullet)
            self.player.tiros_prontos = 10


class SistemaInimigosAsteroid(SistemaInimigos):
    def __init__(self, inimigos, player, plataformas, bullets):
        self.plataformas = plataformas
        self.bullets = bullets
        super().__init__(inimigos, player, plataformas)

    def tick(self):
        for enemy in self.get_entidades():
            enemy.rect.x += enemy.direction[0]
            enemy.rect.y += enemy.direction[1]

            entidades_sem_1 = self.get_entidades().copy()
            entidades_sem_1.remove(enemy)
            for enemy_2 in entidades_sem_1:
                if enemy.rect.colliderect(enemy_2.rect):
                    enemy_2.direction[0] *= -1
                    enemy_2.direction[1] *= -1

            if self.player.rect.colliderect(enemy.rect) and not self.player.is_invincible:
                self.player.tomar_dano()

            if enemy.rect.x + enemy.rect.width > 1200 or enemy.rect.x < 0:
                enemy.direction[0] *= -1
            if enemy.rect.y + enemy.rect.height > 650 or enemy.rect.y < 70:
                enemy.direction[1] *= -1
            for plataforma in self.plataformas:
                if enemy.rect.colliderect(plataforma):
                    enemy.direction[0] *= -1
                    enemy.direction[1] *= -1
            for bullet in self.bullets.get_entidades():
                if bullet.rect.colliderect(enemy):
                    self.remover_entidade(enemy)
                    self.removed.append(enemy)


#---------------------------------------------------DINO---------------------------------------------------#


class PlayerDinoSistema(SistemaPlayer):
    def tick(self):
        self.recarga()
        if self.player.rect.x > 180:
            self.player.rect.x -= 18
            self.player.velocity = 4
            self.player.is_invincible = True
            self.player.invincible_ticks = pygame.time.get_ticks()
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not self.player.is_jumping:
                self.player.jump()
            if self.player.is_invincible:
                if pygame.time.get_ticks() - self.player.invincible_ticks > self.player.invincible_duration:
                    self.player.is_invincible = False


class SistemaInimigosDino(SistemaInimigos):
    def tick(self):
        for enemy in self.get_entidades():
            enemy.rect.x -= 3

            entidades_sem_1 = self.get_entidades().copy()
            entidades_sem_1.remove(enemy)
            for enemy_2 in entidades_sem_1:
                if enemy.rect.colliderect(enemy_2.rect):
                    if enemy.rect.y == enemy_2.rect.y:
                        enemy_2.direction[0] *= -1
                    elif enemy.rect.y > enemy_2.rect.y:
                        enemy_2.velocity = -10

            if enemy.rect.x < 0:
                enemy.rect.x = 1200
            if enemy.rect.x > 1200:
                enemy.rect.x = 0

            if self.player.rect.colliderect(enemy.rect):
                if self.player.is_jumping:
                    self.player.jump()
                    self.removed.append(enemy)
                    self.remover_entidade(enemy)
                elif not self.player.is_invincible:
                    self.player.tomar_dano()


#---------------------------------------------------FLAPPY---------------------------------------------------#


class PlayerFlappySistema(SistemaPlayer):
    def tick(self):
        self.recarga()
        self.player.vel_x = 3.5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player.jump_flappy()


class SistemaInimigosFlappy(SistemaInimigos):
    def tick(self):
        for plataforma in self.plataformas:
            if self.player.rect.colliderect(plataforma):
                self.player.tomar_dano()
                self.player.rect.y = 200
                self.player.velocity = 0

        for enemy in self.get_entidades():
            entidades_sem_1 = self.get_entidades().copy()
            entidades_sem_1.remove(enemy)
            for enemy_2 in entidades_sem_1:
                if enemy.rect.colliderect(enemy_2.rect):
                    if enemy.rect.y > enemy_2.rect.y:
                        enemy_2.rect.y -= 10
            if self.player.rect.colliderect(enemy.rect):
                self.removed.append(enemy)
                self.remover_entidade(enemy)
            for plataforma in self.plataformas:
                if enemy.rect.colliderect(plataforma):
                    enemy.rect.y -= 10


#---------------------------------------------------MARIO---------------------------------------------------#


class PlayerMarioSistema(SistemaPlayer):
    def tick(self):
        self.recarga()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.vel_x = -5
            self.player.animate_run()
        if keys[pygame.K_d]:
            self.player.vel_x = 5
            self.player.animate_run()
        if not(keys[pygame.K_a] or keys[pygame.K_d]):
            self.player.is_running = False
        if keys[pygame.K_SPACE] and not self.player.is_jumping:
            self.player.jump()


class SistemaInimigosMario(SistemaInimigos):
    def tick(self):
        for enemy in self.get_entidades():
            enemy.rect.x += enemy.direction[0]

            entidades_sem_1 = self.get_entidades().copy()
            entidades_sem_1.remove(enemy)
            for enemy_2 in entidades_sem_1:
                if enemy.rect.colliderect(enemy_2.rect):
                    if enemy.rect.y == enemy_2.rect.y:
                        enemy_2.direction[0] *= -1
                    elif enemy.rect.y > enemy_2.rect.y:
                        enemy_2.velocity = -10
            if enemy.rect.x + enemy.rect.width > 1200 or enemy.rect.x < 0:
                enemy.direction[0] *= -1
            if self.player.rect.colliderect(enemy.rect):
                if self.player.is_jumping:
                    self.player.jump()
                    self.removed.append(enemy)
                    self.remover_entidade(enemy)
                elif not self.player.is_invincible:
                    self.player.tomar_dano()


#---------------------------------------------------SHOOTER---------------------------------------------------#


class PlayerShooterSistema(SistemaPlayer):
    def tick(self):
        self.recarga()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.rect.x -= 4
        if keys[pygame.K_d]:
            self.player.rect.x += 4
        if keys[pygame.K_w]:
            self.player.rect.y -= 4
        if keys[pygame.K_s]:
            self.player.rect.y += 4


class SistemaInimigosShooter(SistemaInimigos):
    def tick(self):
        for enemy in self.get_entidades():
            enemy.rect.x += enemy.direction[0]
            enemy.rect.y += enemy.direction[1]

            entidades_sem_1 = self.get_entidades().copy()
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

            for plataforma in self.plataformas:
                if enemy.rect.colliderect(plataforma):
                    enemy.direction[0] *= -1
                    enemy.direction[1] *= -1


#---------------------------------------------------SPACE---------------------------------------------------#


class PlayerSpaceSistema(SistemaPlayer):
    def tick(self):
        self.recarga()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.rect.x -= 4
        if keys[pygame.K_d]:
            self.player.rect.x += 4
        if keys[pygame.K_SPACE]:
            self.shoot()
        if self.player.tiros_prontos > 0:
            self.player.tiros_prontos -= 1
        self.update_bullets()

    def update_bullets(self):
        for bullet in self.get_entidades():
            bullet.rect.y -= 10

    def shoot(self):
        if self.player.tiros_prontos == 0:
            bullet = Bullet(self.player.rect.x, self.player.rect.y, 0, -1)
            self.adicionar_entidade(bullet)
            self.player.tiros_prontos = 10


class InimigosSpaceSistema(SistemaInimigos):
    def __init__(self, inimigos, player, plataformas, bullets):
        self.plataformas = plataformas
        self.bullets = bullets
        super().__init__(inimigos, player, plataformas)

    def tick(self):
        for enemy in self.get_entidades():
            enemy.rect.x += enemy.direction[0]*2

            entidades_sem_1 = self.get_entidades().copy()
            entidades_sem_1.remove(enemy)
            for enemy_2 in entidades_sem_1:

                if enemy.rect.colliderect(enemy_2.rect) :
                    if enemy.rect.y > enemy_2.rect.y:
                        enemy.rect.y += (abs(enemy.rect.y - enemy_2.rect.y) + 5)
                        enemy.direction[0] *= -1
                    elif enemy.rect.x > enemy_2.rect.x:
                        enemy.rect.y += (abs(enemy.rect.y - enemy_2.rect.y) + 5)
                        enemy.direction[0] *= -1

            if (self.player.rect.colliderect(enemy.rect) or enemy.rect.y + enemy.rect.height > 650) and not self.player.is_invincible:
                self.player.tomar_dano()
                self.remover_entidade(enemy)
                self.removed.append(enemy)

            if enemy.rect.x + enemy.rect.width > 1200 or enemy.rect.x < 0:
                enemy.direction[0] *= -1
                enemy.rect.y += 50
            
            for plataforma in self.plataformas:
                if enemy.rect.colliderect(plataforma):
                    enemy.direction[0] *= -1
                    enemy.direction[1] *= -1

            for bullet in self.bullets.get_entidades():
                if bullet.rect.colliderect(enemy):
                    self.remover_entidade(enemy)
                    self.removed.append(enemy)


#---------------------------------------------------OUTROS---------------------------------------------------#


class SistemaMovimento(Sistema):
    def __init__(self, listas, player, plataformas):
        super().__init__([])
        self.plataformas = plataformas
        self.adicionar_entidade(player)
        for lista in listas:
            self.adicionar_sistema(lista)

    def tick(self):
        for entidade in self.get_entidades():
            entidade.rect.x += entidade.vel_x
            for plataforma in self.plataformas.get_entidades():
                if entidade.rect.colliderect(plataforma):
                    entidade.rect.x -= entidade.vel_x
                    break
            if entidade.vel_x > 0:
                entidade.vel_x = max(0, entidade.vel_x - entidade.acceleration)
            elif entidade.vel_x < 0:
                entidade.vel_x = min(0, entidade.vel_x + entidade.acceleration)
            if entidade.vel_y > 0:
                entidade.vel_y = max(0, entidade.vel_y - entidade.acceleration)
            elif entidade.vel_y < 0:
                entidade.vel_y = min(0, entidade.vel_y + entidade.acceleration)


class SistemaPlataformas(Sistema):
    def __init__(self, lista):
        super().__init__([])
        for plataforma in lista:
            self.adicionar_entidade(plataforma)

    def tick(self):
        pass


class SistemaDesenho(Sistema):
    def __init__(self, lista_sistemas, player, screen):
        self.__screen = screen
        self.player = player
        super().__init__([])
        self.adicionar_entidade(player)
        for sistema in lista_sistemas:
            self.adicionar_sistema(sistema)

    def tick(self):
        self.player.update()
        for entidade in self.get_entidades():
            entidade.update()
            self.__screen.blit(entidade.image, entidade.rect)


class SistemaGravidade(Sistema):
    def __init__(self, player, plataformas, gravidade, inimigos=[]):
        super().__init__([])
        self.__plataformas = plataformas
        self.gravidade = gravidade
        if (inimigos != []):
            self.adicionar_sistema(inimigos)
        self.adicionar_entidade(player)

    def tick(self):
        for entidade in self.get_entidades():
            entidade.rect.y += entidade.velocity
            entidade.velocity += self.gravidade
            for plataforma in self.__plataformas:
                if entidade.rect.colliderect(plataforma):
                    # Check if collide is in platform bottom
                    if entidade.rect.y + entidade.height > plataforma.rect.bottom:
                        entidade.rect.y = plataforma.rect.bottom
                    else:
                        entidade.is_jumping = False
                        entidade.rect.y = plataforma.rect.y - entidade.height
                        entidade.velocity = 0
                    break


class SistemaPlayerTrocaLadoHorizontal(SistemaPlayer):
    def tick(self):
        if self.player.rect.x < - (self.player.width/2):
            self.player.rect.x = 1200 - (self.player.width/2)
        elif self.player.rect.x > 1200 - (self.player.width/2):
            self.player.rect.x = - (self.player.width/2)


class SistemaPlayerTrocaLadoVertical(SistemaPlayer):
    def tick(self):
        if self.player.rect.y < 70:  # altura da hud
            self.player.rect.y = 650 - self.player.height
        elif self.player.rect.y > (650 - self.player.height):  # altura plataforma
            self.player.rect.y = 70


class SistemaPlayerBateParedeHorizontal(SistemaPlayer):
    def tick(self):
        if self.player.rect.x < 0:
            self.player.rect.x = 0
        elif self.player.rect.x > 1200 - self.player.width:
            self.player.rect.x = 1200 - self.player.width


class SistemaPlayerBateParedeVertical(SistemaPlayer):
    def tick(self):
        if self.player.rect.y < 60:
            self.player.rect.y = 60
            self.player.velocity = 0
        elif self.player.rect.y > (650 - self.player.height):
            self.player.rect.y = 650 - self.player.height
