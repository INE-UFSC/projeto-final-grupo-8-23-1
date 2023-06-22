import pygame
import random
import time

from entidade import Player, Platform
from mario import Mario
from shooter import Shooter
from flappy import Flappy

from hud import Hud
from gameover import GameOver
from menu import Menu


class Controlador:
    def __init__(self, screen):
        pygame.display.set_caption("RetroVerse")
        self.jogos = {'Mario': Mario, 'Shooter': Shooter, 'Flappy': Flappy}
        self.jogo_atual = random.choice(list(self.jogos.values()))
        self.screen = screen
        self.hud = Hud()
        self.player = Player()
        self.plataforma = [Platform()]
        self.tempo_troca_de_fase = 10
        self.font = pygame.font.Font(None, 36)
        self.running = True
        self.jogos_disponiveis = list(self.jogos.values()).copy()
        self.inicio_jogo = time.time()
        self.tempo_na_fase = 0
        self.score = 0
        self.temp_score = 0
        self.player.lives = 3
        self.num_fases = 0
        self.tempo_na_fase = 0
        self.inimigos = []
        self.tempo = 0
        self.configurar()

    def set_jogo(self, jogo_nome):
        self.jogo_atual = self.jogos[jogo_nome]

    def configurar(self):
        self.jogos_disponiveis = list(self.jogos.values()).copy()
        self.inicio_jogo = time.time()
        self.tempo_na_fase = 0
        self.pontuacao = 0
        self.player.lives = 3
        self.num_fases = 0
        self.tempo_na_fase = 0
        self.inimigos = []
        self.tempo = 0

    def contar_tempo(self):
        self.tempo = time.time() - self.inicio_jogo
        self.tempo_na_fase = self.tempo - self.tempo_troca_de_fase * self.num_fases

    def contar_pontuacao(self):
        self.temp_score = self.novo_jogo.get_score()

    def mudar_jogo(self):
        if len(self.jogos_disponiveis) == 1:
            self.jogos_disponiveis = list(self.jogos.values()).copy()
        self.jogos_disponiveis.remove(self.jogo_atual)
        self.jogo_atual = random.choice(self.jogos_disponiveis)
        self.num_fases += 1

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.contar_tempo()
        self.contar_pontuacao()
        self.hud.update()

    def refazer_inimigos(self):
        self.inimigos = self.novo_jogo.get_inimigos()
        self.player = self.novo_jogo.get_player()
        self.plataforma = self.novo_jogo.get_plataformas()
        self.novo_jogo = self.jogo_atual(self.screen, [], self.player, self.inimigos, self.plataforma)

    def game_over_reset(self):
        self.jogos_disponiveis = list(self.jogos.values()).copy()
        gameover_screen = GameOver(self.screen, self.pontuacao, self)
        nome_jogo = gameover_screen.run()
        self.running = False
        if nome_jogo in self.jogos:
            self.jogo_atual = self.jogos[nome_jogo]
            self.novo_jogo = self.jogo_atual(self.screen, [], self.player, self.inimigos, self.plataforma)
            self.running = True
        self.inicio_jogo = time.time()
        self.player.lives = 3
        self.num_fases = 0

    def run(self):
        menu = Menu(self.screen)
        nome_jogo = menu.main()
        self.jogo_atual = self.jogos[nome_jogo]
        self.novo_jogo = self.jogo_atual(self.screen, [], self.player, self.inimigos, self.plataforma)
        self.inicio_jogo = time.time()
        while self.running:
            self.screen.fill((0, 0, 0))
            self.novo_jogo.run()
            self.hud.draw(self.screen, self.player.lives, self.tempo_troca_de_fase,
                          self.tempo_na_fase, self.tempo,
                          self.score + self.temp_score)
            self.update()
            pygame.display.flip()
            if self.tempo_na_fase >= self.tempo_troca_de_fase:
                self.score += self.temp_score
                self.score += 100
                self.mudar_jogo()
                self.refazer_inimigos()
            if self.player.lives <= 0:
                self.game_over_reset()
        pygame.quit()
