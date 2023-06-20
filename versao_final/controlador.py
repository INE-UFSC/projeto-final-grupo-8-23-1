import pygame
import random
import time 

from entidade import Enemy, Player, Platform

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
        self.hud = Hud(self)
        self.player = Player()
        self.plataforma = [Platform()]
        self.tempo_troca_de_fase = 5
        self.font = pygame.font.Font(None, 36)
        self.running = True
        self.jogos_disponiveis = list(self.jogos.values()).copy()
        self.inicio_jogo = time.time()
        self.tempo_na_fase = 0
        self.pontuacao = 0
        self.player.lives = 3
        self.num_fases = 0
        self.tempo_na_fase = 0
        self.inimigos = []
        self.tempo = 0
        self.configurar()

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
         
    def set_jogo(self, jogo_nome):
        self.jogo_atual = self.jogos[jogo_nome]

    def contar_tempo(self):
        self.tempo = time.time() - self.inicio_jogo
        self.tempo_na_fase = self.tempo - self.tempo_troca_de_fase * self.num_fases

    def contar_pontuacao(self):
        # contar_pontuacao
        pass

    def mudar_jogo(self):
        self.jogos_disponiveis.remove(self.jogo_atual)
        if len(self.jogos_disponiveis) == 0:
            self.jogos_disponiveis = list(self.jogos.values()).copy()
        self.jogo_atual = random.choice(self.jogos_disponiveis)
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
        jogo = self.jogo_atual(self.screen, [], self.player, self.inimigos, self.plataforma)
        self.inicio_jogo = time.time() # começa a contar o tempo
        while self.running:
            self.screen.fill((0, 0, 0))
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
                if nome_jogo in self.jogos:
                    self.jogo_atual = self.jogos[nome_jogo]
                    jogo = self.jogo_atual(self.screen, [], self.player, self.inimigos, self.plataforma)
                    self.running = True
                self.configurar()

        pygame.quit()
