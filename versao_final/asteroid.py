from sistemas import SistemaDesenho, SistemaInimigosAsteroid,\
     SistemaPlataformas, PlayerAsteroidSistema, SistemaMovimento, SistemaPlayerTrocaLadoHorizontal, SistemaPlayerTrocaLadoVertical
from jogoabstrato import JogoAbstrato
import random
from entidade import Enemy


class Asteroid(JogoAbstrato):
    def inimigo(self):
        return Enemy(random.uniform(100, 1100), random.uniform(100, 550), (255, 0, 255))

    def inicializar_sistemas(self):
        self.sistemas.append(PlayerAsteroidSistema(self.player))

        self.inimigos_sys = SistemaInimigosAsteroid(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        self.sistemas.append(SistemaPlayerTrocaLadoHorizontal(self.player))
        self.sistemas.append(SistemaPlayerTrocaLadoVertical(self.player))

        super().inicializar_sistemas()
