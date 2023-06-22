from sistemas import SistemaDesenho, SistemaInimigosAsteroid,\
     SistemaPlataformas, PlayerAsteroidSistema, SistemaMovimento, SistemaPlayerTrocaLadoHorizontal, SistemaPlayerTrocaLadoVertical
from jogoabstrato import JogoAbstrato


class Asteroid(JogoAbstrato):
    def inicializar_sistemas(self):
        self.sistemas.append(PlayerAsteroidSistema(self.player))

        self.inimigos_sys = SistemaInimigosAsteroid(self.inimigos, self.player)
        self.sistemas.append(self.inimigos_sys)

        plataformas = SistemaPlataformas(self.plataformas)
        self.sistemas.append(plataformas)

        desenho = SistemaDesenho([plataformas, self.inimigos_sys], self.player, self.screen)
        self.sistemas.append(desenho)

        movimento = SistemaMovimento([self.inimigos_sys], self.player)
        self.sistemas.append(movimento)

        self.sistemas.append(SistemaPlayerTrocaLadoHorizontal(self.player))

        self.sistemas.append(SistemaPlayerTrocaLadoVertical(self.player))
