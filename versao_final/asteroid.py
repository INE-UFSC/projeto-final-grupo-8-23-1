from sistemas import SistemaDesenho, SistemaInimigosAsteroid,\
     SistemaPlataformas, PlayerAsteroidSistema, SistemaMovimento, SistemaPlayerTrocaLadoHorizontal, SistemaPlayerTrocaLadoVertical
from jogoabstrato import JogoAbstrato
import random
from entidade import Enemy


class Asteroid(JogoAbstrato):
    def inimigo(self, x, y):
        return Enemy(x, y, (255, 0, 255))

    def inicializar_sistemas(self):
        asteroid = PlayerAsteroidSistema(self.player)
        self.sistemas.append(asteroid)

        self.inimigos_sys = SistemaInimigosAsteroid(self.inimigos, self.player, asteroid)
        self.sistemas.append(self.inimigos_sys)

        self.sistemas.append(SistemaPlayerTrocaLadoHorizontal(self.player))
        self.sistemas.append(SistemaPlayerTrocaLadoVertical(self.player))

        super().inicializar_sistemas([asteroid])
