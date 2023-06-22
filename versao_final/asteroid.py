import random
from entidade import Enemy
from sistemas import SistemaDesenho, SistemaInimigosAsteroid,\
     SistemaPlataformas, PlayerAsteroidSistema, SistemaMovimento, SistemaPlayerTrocaLadoHorizontal, SistemaPlayerTrocaLadoVertical
from jogoabstrato import JogoAbstrato


class Asteroid(JogoAbstrato):
    def __init__(self, screen, entidades, player, inimigos, plataformas):
        self.entidades = []
        super().__init__(screen, entidades, player, inimigos, plataformas)

    def inicializar_entidades(self, entidades=[]):
        if len(self.inimigos) < 5:
            for _ in range(5 - len(self.inimigos)):
                self.inimigos.append(Enemy(random.uniform(100, 1100), random.uniform(100, 550), (255, 0, 255)))
        self.entidades.append(self.player)
        for inimigo in self.inimigos:
            self.entidades.append(inimigo)
        for plataforma in self.plataformas:
            self.entidades.append(plataforma)

    def inicializar_sistemas(self):
        self.sistemas = []

        self.player_sys = PlayerAsteroidSistema(self.player)
        self.sistemas.append(self.player_sys)

        self.inimigos_sys = SistemaInimigosAsteroid(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        plataformas = SistemaPlataformas(self.plataformas)
        self.sistemas.append(plataformas)

        desenho = SistemaDesenho([plataformas, self.inimigos_sys], self.player, self.screen)
        self.sistemas.append(desenho)

        movimento = SistemaMovimento([self.inimigos_sys], self.player)
        self.sistemas.append(movimento)

        playertrocaladohorizontal = SistemaPlayerTrocaLadoHorizontal(self.player)
        self.sistemas.append(playertrocaladohorizontal)

        playertrocaladovertical = SistemaPlayerTrocaLadoVertical(self.player)
        self.sistemas.append(playertrocaladovertical)