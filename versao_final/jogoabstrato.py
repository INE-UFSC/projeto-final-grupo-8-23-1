import pygame
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
        if len(self.inimigos) < 5:
            for _ in range(5 - len(self.inimigos)):
                self.inimigos.append(self.inimigo())
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
