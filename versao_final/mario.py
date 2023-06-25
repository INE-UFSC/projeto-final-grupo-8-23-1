from sistemas import SistemaInimigosMario, SistemaGravidade,\
        PlayerMarioSistema, SistemaPlayerBateParedeHorizontal
from jogoabstrato import JogoAbstrato
from entidade import PlayerMario, MarioEnemy


class Mario(JogoAbstrato):
    def trocar_player(self, player):
        self.player = PlayerMario(player.width, player.height, player.rect.x, player.rect.y, player.color)

    def inimigo(self, x, y):
        return MarioEnemy(x, y, (255, 0, 0))

    def inicializar_sistemas(self):
        self.inimigos_sys = SistemaInimigosMario(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        self.sistemas.append(PlayerMarioSistema(self.player))
        self.sistemas.append(SistemaGravidade(self.player, self.plataformas, 0.9, self.inimigos))
        self.sistemas.append(SistemaPlayerBateParedeHorizontal(self.player))

        super().inicializar_sistemas()
