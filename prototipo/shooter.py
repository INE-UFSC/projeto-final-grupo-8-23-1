from entidade import Enemy, Platform, Player
from sistemas import SistemaDesenho, SistemaInimigos,\
    SistemaGravidade, SistemaPlataformas
from jogoabstrato import JogoAbstrato


class Shooter(JogoAbstrato):
    def __init__(self, entidades):
        self.entidades = entidades
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
        self.inimigos = SistemaInimigos([Enemy(300, 500)], self.player)
        self.sistemas.append(self.inimigos)

        gravidade = SistemaGravidade([self.player], self.platform)
        self.sistemas.append(gravidade)

        plataformas = SistemaPlataformas(self.platform)
        self.sistemas.append(plataformas)

        desenho = SistemaDesenho([plataformas, gravidade, self.inimigos], self.player, self.screen)
        self.sistemas.append(desenho)
