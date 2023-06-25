from sistemas import SistemaDesenho, SistemaInimigosAsteroid,\
     SistemaPlataformas, PlayerAsteroidSistema, SistemaMovimento, SistemaPlayerTrocaLadoHorizontal, SistemaPlayerTrocaLadoVertical
from jogoabstrato import JogoAbstrato
import random
from entidade import Enemy


class Asteroid(JogoAbstrato):
    def inimigo(self, x, y):
        return Enemy(x, y, (255, 0, 255))

    def inicializar_sistemas(self):
        self.inimigos_sys = SistemaInimigosAsteroid(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        asteroid = PlayerAsteroidSistema(self.player)
        self.sistemas.append(asteroid)
        self.sistemas.append(SistemaPlayerTrocaLadoHorizontal(self.player))
        self.sistemas.append(SistemaPlayerTrocaLadoVertical(self.player))

        super().inicializar_sistemas([asteroid])
