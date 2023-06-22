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

        gravidade = SistemaGravidade(self.player, self.plataformas, self.inimigos, 0.9)
        self.sistemas.append(gravidade)

        plataformas = SistemaPlataformas(self.plataformas)
        self.sistemas.append(plataformas)

        desenho = SistemaDesenho([plataformas, gravidade, self.inimigos_sys], self.player, self.screen)
        self.sistemas.append(desenho)

        movimento = SistemaMovimento([self.inimigos_sys], self.player)
        self.sistemas.append(movimento)

        sistemaplayerbateparedehorizontal = SistemaPlayerBateParedeHorizontal(self.player)
        self.sistemas.append(sistemaplayerbateparedehorizontal)
