import pygame
import sys
from entidade import Enemy, Platform, Player
from sistemas import SistemaDesenho, SistemaInimigos, SistemaGravidade, SistemaPlataformas
from jogoabstrato import JogoAbstrato


class Game(JogoAbstrato):
    def __init__(self):
        super().__init__()

    def inicializar_entidades(self, entidades=[]):
        self.player = Player()
        self.enemies = [Enemy(300, 500)]
        self.platform = Platform()

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


if __name__ == "__main__":
    game = Game()
    game.run()
