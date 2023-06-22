from sistemas import SistemaDesenho, SistemaInimigosShooter,\
     SistemaPlataformas, PlayerShooterSistema, SistemaMovimento, SistemaPlayerBateParedeVertical, SistemaPlayerBateParedeHorizontal
from jogoabstrato import JogoAbstrato
import random
from entidade import Enemy


class Shooter(JogoAbstrato):
    def inimigo(self):
        return Enemy(random.uniform(100, 1100), random.uniform(100, 550), (0, 255, 0))

    def inicializar_sistemas(self):
        self.inimigos_sys = SistemaInimigosShooter(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        self.sistemas.append(PlayerShooterSistema(self.player))
        self.sistemas.append(SistemaPlayerBateParedeVertical(self.player))
        self.sistemas.append(SistemaPlayerBateParedeHorizontal(self.player))

        super().inicializar_sistemas()
