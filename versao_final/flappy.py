from sistemas import SistemaGravidade, SistemaDesenho, SistemaInimigosFlappy, SistemaPlayerBateParedeVertical,\
     SistemaPlataformas, PlayerFlappySistema, SistemaMovimento, SistemaPlayerTrocaLadoHorizontal
from jogoabstrato import JogoAbstrato
from entidade import Enemy
import random


class Flappy(JogoAbstrato):
    def __init__(self, screen, entidades, player, inimigos, plataformas):
        super().__init__(screen, entidades, player, inimigos, plataformas)
        player.rect.y = 200
        player.vel_y = 0

    def inimigo(self):
        return Enemy(random.uniform(100, 1100), random.uniform(100, 550), (0, 0, 255))

    def inicializar_sistemas(self):
        self.player_sys = PlayerFlappySistema(self.player)
        self.sistemas.append(self.player_sys)

        self.inimigos_sys = SistemaInimigosFlappy(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        gravidade = SistemaGravidade(self.player, self.plataformas, [], 0.15)
        self.sistemas.append(gravidade)

        playertrocalado = SistemaPlayerTrocaLadoHorizontal(self.player)
        self.sistemas.append(playertrocalado)

        playerbateparede = SistemaPlayerBateParedeVertical(self.player)
        self.sistemas.append(playerbateparede)

        super().inicializar_sistemas()
