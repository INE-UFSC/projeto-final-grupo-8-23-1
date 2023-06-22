from sistemas import SistemaDesenho, SistemaInimigosMario, SistemaGravidade,\
        SistemaPlataformas, PlayerMarioSistema, SistemaMovimento, SistemaPlayerBateParedeHorizontal
from jogoabstrato import JogoAbstrato


class Mario(JogoAbstrato):
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
