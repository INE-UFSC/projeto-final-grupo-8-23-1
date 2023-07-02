from jogoabstrato import JogoAbstrato
from sistemas import InimigosSpaceSistema,PlayerSpaceSistema, SistemaPlayerBateParedeHorizontal, SistemaGravidade
from entidade import InimigoSpace, PlayerSpace


class Space(JogoAbstrato):
    def inimigo(self, x, y):
        return InimigoSpace(x, y, (255, 0, 255))

    def trocar_player(self, player):
        self.player = PlayerSpace(player.width, player.height, player.rect.x, player.rect.y, player.color)

    def inicializar_sistemas(self):
        space = PlayerSpaceSistema(self.player)
        self.sistemas.append(space)

        self.inimigos_sys = InimigosSpaceSistema(self.inimigos, self.player, self.plataformas, space)
        self.sistemas.append(self.inimigos_sys)

        self.sistemas.append(SistemaGravidade(self.player, self.plataformas, 2, []))
        self.sistemas.append(SistemaPlayerBateParedeHorizontal(self.player))

        super().inicializar_sistemas([space])