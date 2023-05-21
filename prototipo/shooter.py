from entidade import Enemy, Platform, Player, ShooterEnemy
from sistemas import SistemaDesenho, SistemaInimigosShooter,\
    SistemaGravidade, SistemaPlataformas, PlayerShooterSistema, SistemaMovimento
from jogoabstrato import JogoAbstrato


class Shooter(JogoAbstrato):
    def __init__(self, entidades):
        self.entidades = entidades
        super().__init__(entidades)

    def inicializar_entidades(self, entidades=[]):
        self.player = Player()
        self.enemies = [ShooterEnemy(300, 500)]
        self.platform = [Platform()]

        self.entidades.append(self.player)
        for inimigo in self.enemies:
            self.entidades.append(inimigo)
        for plataforma in self.platform:
            self.entidades.append(plataforma)

    def inicializar_sistemas(self):
        self.sistemas = []

        self.player_sys = PlayerShooterSistema(self.player)
        self.sistemas.append(self.player_sys)

        self.inimigos = SistemaInimigosShooter(self.enemies, self.player)
        self.sistemas.append(self.inimigos)

        gravidade = SistemaGravidade([self.player], self.platform)
        self.sistemas.append(gravidade)

        plataformas = SistemaPlataformas(self.platform)
        self.sistemas.append(plataformas)

        desenho = SistemaDesenho([plataformas, gravidade, self.inimigos], self.player, self.screen)
        self.sistemas.append(desenho)

        movimento = SistemaMovimento([self.inimigos], self.player)
        self.sistemas.append(movimento)
