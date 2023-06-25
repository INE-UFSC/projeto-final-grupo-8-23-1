from sistemas import SistemaGravidade, SistemaInimigosFlappy,\
    SistemaPlayerBateParedeVertical, PlayerFlappySistema, \
    SistemaPlayerTrocaLadoHorizontal
from jogoabstrato import JogoAbstrato
from entidade import InimigoVoador, PlayerFlappy


class Flappy(JogoAbstrato):
    def __init__(self, screen, entidades, player, inimigos, plataformas):
        super().__init__(screen, entidades, player, inimigos, plataformas)
        player.rect.y = 200
        player.velocity = 0.15

    def trocar_player(self, player):
        self.player = PlayerFlappy(player.width, player.height, player.rect.x, player.rect.y, player.color)

    def inimigo(self, x, y):
        return InimigoVoador(x, y, (0, 255, 0))

    def inicializar_sistemas(self):
        self.inimigos_sys = SistemaInimigosFlappy(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        self.sistemas.append(PlayerFlappySistema(self.player))
        self.sistemas.append(SistemaGravidade(self.player, self.plataformas, 0.15))
        self.sistemas.append(SistemaPlayerTrocaLadoHorizontal(self.player))
        self.sistemas.append(SistemaPlayerBateParedeVertical(self.player))

        super().inicializar_sistemas()
