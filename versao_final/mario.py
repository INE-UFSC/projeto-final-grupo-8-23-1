from sistemas import SistemaDesenho, SistemaInimigosMario, SistemaGravidade,\
        SistemaPlataformas, PlayerMarioSistema, SistemaMovimento, SistemaPlayerBateParedeHorizontal
from jogoabstrato import JogoAbstrato
import random
from entidade import Enemy


class Mario(JogoAbstrato):
    def inimigo(self):
        return Enemy(random.uniform(100, 500), 500, (255, 0, 0))

    def inicializar_sistemas(self):
        self.player_sys = PlayerMarioSistema(self.player)
        self.sistemas.append(self.player_sys)

        self.inimigos_sys = SistemaInimigosMario(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        self.gravidade = SistemaGravidade(self.player, self.plataformas, self.inimigos, 0.9)
        self.sistemas.append(self.gravidade)

        sistemaplayerbateparedehorizontal = SistemaPlayerBateParedeHorizontal(self.player)
        self.sistemas.append(sistemaplayerbateparedehorizontal)

        super().inicializar_sistemas()
