import pygame
import sys
from hud import Hud


class JogoAbstrato:
    def __init__(self, entidades=[]):
        # pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.start_ticks = pygame.time.get_ticks()
        self.hud = Hud(self)

        self.entidades = []
        self.inicializar_entidades()
        self.inicializar_sistemas()

    def rodar_sistemas(self):
        for sistema in self.sistemas:
            sistema.tick()
        list_removed = self.inimigos.check_removed()
        for removed in list_removed:
            for sistema in self.sistemas:
                if removed in sistema.get_entidades():
                    sistema.remover_entidade(removed)

    def run(self):
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

    def get_entidades(self):
        return self.entidades

    def inicializar_entidades(self):
        pass

    def inicializar_sistemas(self):
        pass
