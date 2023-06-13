import pygame
import random

from entidade import Enemy, Player, Platform

from mario import Mario
from shooter import Shooter
from flappy import Flappy

from hud import Hud
from gameover import GameOver
from menu import Menu


class Controlador:
    def __init__(self, screen):
        self.jogos = {'Mario': Mario, 'Shooter': Shooter, 'Flappy': Flappy}
        self.jogo_atual = random.choice(list(self.jogos.values()))
        self.screen = screen
        self.hud = Hud(self)
        self.player = Player()
        self.inimigos = []
        self.plataforma = [Platform()]
        self.tempo = 0
        self.tempo_intermediario = 0
        self.tempo_no_jogo = 0
        self.tempo_na_fase = 0
        self.tempo_troca_de_fase = 5000
        self.configurar()

    def set_jogo(self, jogo_nome):
        self.jogo_atual = self.jogos[jogo_nome]

    def configurar(self):
        self.pontuacao = 0
        self.vidas = 3
        self.num_fases = 0
        self.tempo_na_fase = 0
        pygame.display.set_caption("RetroVerse")
        self.font = pygame.font.Font(None, 36)
        self.running = True

    def contar_tempo(self):
        self.tempo = pygame.time.get_ticks()
        self.tempo_no_jogo = self.tempo - self.tempo_intermediario
        self.tempo_na_fase = self.tempo_no_jogo - self.tempo_troca_de_fase * self.num_fases


    def contar_pontuacao(self):
        # contar_pontuacao
        pass

    def mudar_jogo(self):
        jogos_disponiveis = list(self.jogos.values()).copy()
        jogos_disponiveis.remove(self.jogo_atual)
        self.jogo_atual = random.choice(jogos_disponiveis)
        self.num_fases += 1

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.contar_tempo()
        self.contar_pontuacao()
        self.hud.update()

    def change_enemy(self):
        for inimigo in self.inimigos:
            inimigo.rect.y -= 10

    def run(self):

        menu = Menu(self.screen)
        nome_jogo = menu.main()
        self.jogo_atual = self.jogos[nome_jogo]

        self.tempo_intermediario = pygame.time.get_ticks()
        jogo = self.jogo_atual(self.screen, [], self.player, self.inimigos, self.plataforma)
        while self.running:
            jogo.run()
            self.hud.draw(self.screen)
            self.update()
            pygame.display.flip()
            if self.tempo_na_fase >= self.tempo_troca_de_fase:
                self.mudar_jogo()

                self.inimigos = jogo.get_inimigos()
                self.player = jogo.get_player()
                self.plataforma = jogo.get_plataformas()

                self.change_enemy()

                jogo = self.jogo_atual(self.screen, [], self.player, self.inimigos, self.plataforma)

            if self.player.lives <= 0:
                gameover_screen = GameOver(self.screen, self.pontuacao, self)
                nome_jogo = gameover_screen.run()
                self.running = False
                self.tempo_intermediario = pygame.time.get_ticks()
                if nome_jogo in self.jogos:
                    self.jogo_atual = self.jogos[nome_jogo]
                    jogo = self.jogo_atual(self.screen, [], self.player, self.inimigos, self.plataforma)
                    self.running = True
                self.player.lives = 3

        pygame.quit()
