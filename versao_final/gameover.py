import pygame
from menu import Menu
import sys

class GameOver:
    def __init__(self, screen, pontuacao, controlador):
        self.screen = screen
        self.pontuacao = pontuacao
        self.controlador = controlador
        self.font = pygame.font.Font(None, 55)
        self.highscore = self.carregar_highscore()
        self.gameover_text = pygame.image.load('./assets/gameover2_text.png')
        self.botao_menu = pygame.image.load('./assets/botao_menu.png')
        self.botao_sair = pygame.image.load('./assets/botao_sair.png')
        self.highscore_asset = pygame.image.load('./assets/highscore2.png')
        self.sua_pontuacao_texto = pygame.image.load('./assets/sua_pontuacao_texto.png')
        self.update_highscore()

    def carregar_highscore(self):
        try:
            with open('highscore.txt', 'r') as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def salvar_highscore(self, new_highscore):
        with open('highscore.txt', 'w') as f:
            f.write(str(new_highscore))

    def update_highscore(self):
        if self.pontuacao > self.highscore:
            self.highscore = self.pontuacao
            self.salvar_highscore(self.highscore)

    def draw_score(self):
        score_text = self.font.render(f'{self.pontuacao}', True, (255, 255, 255))
        highscore_text = self.font.render(f'{self.highscore}', True, (255, 255, 255))
        self.screen.blit(self.highscore_asset, (450, 400))
        self.screen.blit(score_text, (750, 405))
        self.screen.blit(self.sua_pontuacao_texto, (450, 500))
        self.screen.blit(highscore_text, (750, 500))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.botao_menu.get_rect(topleft=(375, 250)).collidepoint(x, y):
                        menu = Menu(self.screen)
                        nome_do_jogo = menu.main()
                        print(nome_do_jogo)
                        return nome_do_jogo
                    elif self.botao_sair.get_rect(topleft=(625, 250)).collidepoint(x,
                                                                                   y):  # Adiciona a detecção de clique para o botão sair
                        pygame.quit()
                        sys.exit()

            self.screen.fill((4, 3, 45))
            self.screen.blit(self.gameover_text, (300, 100))
            self.screen.blit(self.botao_menu, (375, 250))
            self.screen.blit(self.botao_sair, (625, 250))
            self.draw_score()
            pygame.display.flip()
