from sistemas import SistemaDesenho, SistemaInimigosShooter,\
     SistemaPlataformas, PlayerShooterSistema, SistemaMovimento, SistemaPlayerBateParedeVertical, SistemaPlayerBateParedeHorizontal
from jogoabstrato import JogoAbstrato


class Shooter(JogoAbstrato):
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

        self.sistemas.append(SistemaPlayerBateParedeVertical(self.player))
        self.sistemas.append(SistemaPlayerBateParedeHorizontal(self.player))
