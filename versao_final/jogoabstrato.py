import pygame
import random
import sys
from sistemas import SistemaDesenho, SistemaMovimento, SistemaPlataformas


class JogoAbstrato:
    def __init__(self, screen, entidades, player, inimigos=[], plataformas=[]):
        self.trocar_player(player)
        self.clock = pygame.time.Clock()
        self.start_ticks = pygame.time.get_ticks()
        self.screen = screen
        self.entidades = []
        self.sistemas = []
        self.score = 0

        self.entidades = entidades
        self.inimigos = inimigos
        self.plataformas = plataformas

        self.inicializar_entidades()
        self.inicializar_sistemas()

    def rodar_sistemas(self):
        for sistema in self.sistemas:
            sistema.tick()
        list_removed = self.inimigos_sys.check_removed()
        for removed in list_removed:
            self.score += 5
            self.inimigos_sys.clear_removed()
            # self.inimigos_sys.adicionar_entidade(self.inimigo())

    def inicializar_entidades(self):
        for _ in range(5 - len(self.inimigos)):
            for _ in range(1000):
                x_novo = random.randint(0, 1150)
                y_novo = random.randint(65, 500)
                if not any(abs(x_novo - inimigo.rect.x) < 55 and abs(y_novo - inimigo.rect.y) < 55 for inimigo in self.inimigos)\
                    and not abs(x_novo - self.player.rect.x) < 150 and not abs(y_novo - self.player.rect.y) < 150:
                    break
            else:
                continue
            self.inimigos.append(self.inimigo(x_novo, y_novo))

        self.entidades.append(self.player)
        for inimigo in self.inimigos:
            self.entidades.append(inimigo)
        for plataforma in self.plataformas:
            self.entidades.append(plataforma)

    def inicializar_sistemas(self, sistemas_desenho=[]):
        plataformas = SistemaPlataformas(self.plataformas)
        self.sistemas.append(plataformas)

        if (sistemas_desenho != []):
            desenho = SistemaDesenho([plataformas, self.inimigos_sys, *sistemas_desenho], self.player, self.screen)
        else:
            desenho = SistemaDesenho([plataformas, self.inimigos_sys], self.player, self.screen)
        self.sistemas.append(desenho)

        movimento = SistemaMovimento([self.inimigos_sys], self.player)
        self.sistemas.append(movimento)

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.rodar_sistemas()

        self.clock.tick(90)

    def get_player(self):
        return self.player

    def get_inimigos(self):
        return self.inimigos

    def get_plataformas(self):
        return self.plataformas

    def get_score(self):
        return self.score

    def inimigo(self):
        pass
