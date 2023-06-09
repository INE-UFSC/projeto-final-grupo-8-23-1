import random
from entidade import Enemy
from sistemas import SistemaDesenho, SistemaInimigosShooter,\
     SistemaPlataformas, PlayerShooterSistema, SistemaMovimento
from jogoabstrato import JogoAbstrato


class Shooter(JogoAbstrato):
    def __init__(self, screen, entidades, player, inimigos, plataformas):
        self.entidades = []
        super().__init__(screen, entidades, player, inimigos, plataformas)

    def inicializar_entidades(self, entidades=[]):
        if len(self.inimigos) < 5:
            for _ in range(5 - len(self.inimigos)):
                self.inimigos.append(Enemy(random.uniform(100, 450), random.uniform(100, 300)))
        self.entidades.append(self.player)
        for inimigo in self.inimigos:
            self.entidades.append(inimigo)
        for plataforma in self.plataformas:
            self.entidades.append(plataforma)

    def inicializar_sistemas(self):
        self.sistemas = []

        self.player_sys = PlayerShooterSistema(self.player)
        self.sistemas.append(self.player_sys)

        self.inimigos_sys = SistemaInimigosShooter(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        plataformas = SistemaPlataformas(self.plataformas)
        self.sistemas.append(plataformas)

        desenho = SistemaDesenho([plataformas, self.inimigos_sys], self.player, self.screen)
        self.sistemas.append(desenho)

        movimento = SistemaMovimento([self.inimigos_sys], self.player)
        self.sistemas.append(movimento)
