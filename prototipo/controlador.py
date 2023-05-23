import pygame
import random
from entidade import Enemy, Player, Platform
from mario import Mario
from shooter import Shooter


class Controlador:
    def __init__(self):
        self.jogos = [Mario, Shooter]
        self.jogo_atual = random.choice(self.jogos)
        self.screen = pygame.display.set_mode((800, 600))
        self.player = Player()
        self.inimigos = []
        self.plataforma = [Platform()]
        self.configurar()

    def configurar(self):
        self.pontuacao = 0
        self.tempo = 0
        self.vidas = 3
        self.num_fases = 0
        self.tempo_na_fase = 0
        self.tempo_troca_de_fase = 5000
        pygame.display.set_caption("RetroVerse")
        self.font = pygame.font.Font(None, 36)
        self.running = True

    def contar_tempo(self):
        self.tempo = pygame.time.get_ticks()
        self.tempo_na_fase = self.tempo - self.tempo_troca_de_fase * self.num_fases

    def contar_pontuacao(self):
        # contar_pontuacao
        pass

    def mudar_jogo(self):
        jogos_disponiveis = self.jogos.copy()
        jogos_disponiveis.remove(self.jogo_atual)
        self.jogo_atual = random.choice(jogos_disponiveis)
        self.num_fases += 1

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.contar_tempo()
        self.contar_pontuacao()

    def change_enemy(self):
        for inimigo in self.inimigos:
                inimigo.rect.y -= 10

    def run(self):
        jogo = self.jogo_atual(self.screen, [], self.player, self.inimigos, self.plataforma)
        while self.running:
            jogo.run()
            self.update()
            if self.tempo_na_fase >= self.tempo_troca_de_fase:
                self.mudar_jogo()

                self.inimigos = jogo.get_inimigos()
                self.player = jogo.get_player()
                self.plataforma = jogo.get_plataformas()

                self.change_enemy()

                jogo = self.jogo_atual(self.screen, [], self.player, self.inimigos, self.plataforma)
        pygame.quit()
