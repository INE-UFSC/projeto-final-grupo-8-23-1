from sistemas import SistemaDesenho, SistemaInimigosMario, SistemaGravidade,\
        SistemaPlataformas, PlayerMarioSistema, SistemaMovimento, SistemaPlayerBateParedeHorizontal
from jogoabstrato import JogoAbstrato
import random
from entidade import Enemy


class Mario(JogoAbstrato):
    def inimigo(self, x, y):
        return Enemy(x, y, (255, 0, 0))

    def inicializar_sistemas(self):
        self.inimigos_sys = SistemaInimigosMario(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        self.sistemas.append(PlayerMarioSistema(self.player))
        self.sistemas.append(SistemaGravidade(self.player, self.plataformas, 0.9, self.inimigos))
        self.sistemas.append(SistemaPlayerBateParedeHorizontal(self.player))

        super().inicializar_sistemas()
