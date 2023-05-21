import pygame
import random
from mario import Mario
from shooter import Shooter


class Controlador:
    def __init__(self):

        self.jogos = [Mario, Shooter]
        self.jogo_atual = random.choice(self.jogos)

        self.pontuacao = 0
        self.tempo = 0
        self.vidas = 3

        self.num_fases = 0
        self.tempo_na_fase = 0
        self.tempo_troca_de_fase = 10000

        self.entidades = []

        comprimento_tela = 900
        altura_tela = 600
        self.janela = pygame.display.set_mode((comprimento_tela, altura_tela))
        pygame.display.set_caption("RetroVerse")

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

    def run(self):
        jogo = self.jogo_atual([])
        while self.running:
            jogo.run()
            self.update()
            # jogo.update(self.tempo, self.tempo_na_fase, self.num_fases)
            if self.tempo_na_fase >= self.tempo_troca_de_fase:
                self.entidades = jogo.get_entidades
                self.mudar_jogo()
                jogo = self.jogo_atual(self.entidades)
        pygame.quit()
