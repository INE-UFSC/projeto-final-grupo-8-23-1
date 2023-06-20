import random
from entidade import Enemy
from sistemas import SistemaGravidade, SistemaDesenho, SistemaInimigosFlappy,\
     SistemaPlataformas, PlayerFlappySistema, SistemaMovimento, SistemaTrocaLado
from jogoabstrato import JogoAbstrato


class Flappy(JogoAbstrato):
    def __init__(self, screen, entidades, player, inimigos, plataformas):
        self.entidades = []
        super().__init__(screen, entidades, player, inimigos, plataformas)
        player.rect.y -= 150

    def inicializar_entidades(self, entidades=[]):
        if len(self.inimigos) < 5:
            for _ in range(5 - len(self.inimigos)):
                self.inimigos.append(Enemy(random.uniform(100, 1100), random.uniform(100, 550), (0, 0, 255)))
        self.entidades.append(self.player)
        for inimigo in self.inimigos:
            self.entidades.append(inimigo)
        for plataforma in self.plataformas:
            self.entidades.append(plataforma)

    def inicializar_sistemas(self):
        self.sistemas = []

        self.player_sys = PlayerFlappySistema(self.player)
        self.sistemas.append(self.player_sys)

        self.inimigos_sys = SistemaInimigosFlappy(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        plataformas = SistemaPlataformas(self.plataformas)
        self.sistemas.append(plataformas)

        gravidade = SistemaGravidade(self.player, self.plataformas, [], 0.2)
        self.sistemas.append(gravidade)

        desenho = SistemaDesenho([plataformas, self.inimigos_sys], self.player, self.screen)
        self.sistemas.append(desenho)

        movimento = SistemaMovimento([self.inimigos_sys], self.player)
        self.sistemas.append(movimento)

        trocalado = SistemaTrocaLado(self.player)
        self.sistemas.append(trocalado)