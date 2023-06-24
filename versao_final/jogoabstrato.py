import pygame
import random
import sys
from sistemas import SistemaDesenho, SistemaMovimento, SistemaPlataformas


class JogoAbstrato:
    def __init__(self, screen, entidades, player, inimigos=[], plataformas=[]):
        self.clock = pygame.time.Clock()
        self.start_ticks = pygame.time.get_ticks()
        self.screen = screen
        self.entidades = []
        self.sistemas = []
        self.score = 0

        self.entidades = entidades
        self.player = player
        self.inimigos = inimigos
        self.plataformas = plataformas

        self.inicializar_entidades()
        self.inicializar_sistemas()

    def rodar_sistemas(self):
        for sistema in self.sistemas:
            sistema.tick()
        list_removed = self.inimigos_sys.check_removed()
        for removed in list_removed:
            for sistema in self.sistemas:
                if removed in sistema.get_entidades():
                    self.score += 5
                    sistema.remover_entidade(removed)

    def inicializar_entidades(self, entidades=[]):
        for _ in range(10 - len(self.inimigos)):
            x_novo = random.randint(0, 1150)
            y_novo = random.randint(65, 500)

            for i in range (len(self.inimigos)):
                x_existente = self.inimigos[i].rect.x
                y_existente = self.inimigos[i].rect.y

                if abs(x_novo - x_existente) < 50 and abs(y_novo - y_existente) < 50:
                    x_novo = random.randint(0, 1150)
                    y_novo = random.randint(65, 500)
                    i = 0
            
            self.inimigos.append(self.inimigo(x_novo, y_novo))

        self.entidades.append(self.player)
        for inimigo in self.inimigos:
            self.entidades.append(inimigo)
        for plataforma in self.plataformas:
            self.entidades.append(plataforma)

    def inicializar_sistemas(self):
        plataformas = SistemaPlataformas(self.plataformas)
        self.sistemas.append(plataformas)

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
