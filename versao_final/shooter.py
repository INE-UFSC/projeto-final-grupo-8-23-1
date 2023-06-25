from sistemas import SistemaDesenho, SistemaInimigosShooter,\
     SistemaPlataformas, PlayerShooterSistema, SistemaMovimento, SistemaPlayerBateParedeVertical, SistemaPlayerBateParedeHorizontal
from jogoabstrato import JogoAbstrato
import random
from entidade import InimigoVoador, PlayerShooter


class Shooter(JogoAbstrato):
    def trocar_player(self, player):
        self.player = PlayerShooter(player.width, player.height, player.rect.x, player.rect.y, player.color)

    def inimigo(self, x, y):
        return InimigoVoador(x, y, (0, 255, 0))

    def inicializar_sistemas(self):
        self.inimigos_sys = SistemaInimigosShooter(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        self.sistemas.append(PlayerShooterSistema(self.player))
        self.sistemas.append(SistemaPlayerBateParedeVertical(self.player))
        self.sistemas.append(SistemaPlayerBateParedeHorizontal(self.player))

        super().inicializar_sistemas()
