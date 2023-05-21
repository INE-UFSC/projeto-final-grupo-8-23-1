from entidade import Enemy, Platform, Player
from sistemas import SistemaDesenho, SistemaInimigosMario, SistemaGravidade,\
        SistemaPlataformas, PlayerMarioSistema
from jogoabstrato import JogoAbstrato


class Mario(JogoAbstrato):
    def __init__(self, entidades=[]):
        super().__init__(entidades)

    def inicializar_entidades(self, entidades=[]):
        self.player = Player()
        self.enemies = [Enemy(300, 500)]
        self.platform = [Platform()]

        self.entidades.append(self.player)
        for inimigo in self.enemies:
            self.entidades.append(inimigo)
        for plataforma in self.platform:
            self.entidades.append(plataforma)

    def inicializar_sistemas(self):
        self.sistemas = []

        self.player_sys = PlayerMarioSistema(self.player)
        self.sistemas.append(self.player_sys)

        self.inimigos = SistemaInimigosMario(self.enemies, self.player)
        self.sistemas.append(self.inimigos)

        gravidade = SistemaGravidade([self.player], self.platform)
        self.sistemas.append(gravidade)

        plataformas = SistemaPlataformas(self.platform)
        self.sistemas.append(plataformas)

        desenho = SistemaDesenho([plataformas, gravidade, self.inimigos], self.player, self.screen)
        self.sistemas.append(desenho)
