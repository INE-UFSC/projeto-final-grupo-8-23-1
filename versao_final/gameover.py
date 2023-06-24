import pygame
from menu import Menu
import sys
from highscore import Highscore

class GameOver:
    def __init__(self, screen, score, controlador):
        self.screen = screen
        self.score = score
        self.controlador = controlador
        self.highscore_manager = Highscore()
        self.font = pygame.font.Font(None, 55)
        self.gameover_text = pygame.image.load('versao_final/assets/gameover2_text.png')
        self.botao_menu = pygame.image.load('versao_final/assets/botao_menu.png')
        self.botao_sair = pygame.image.load('versao_final/assets/botao_sair.png')
        self.highscore_asset = pygame.image.load('versao_final/assets/highscore2.png')
        self.sua_score_texto = pygame.image.load('versao_final/assets/sua_pontuacao_texto.png')
        self.highscore_manager.update_highscore(self.score)

    def draw_score(self):
        score_text = self.font.render(f'{self.highscore_manager.highscore}', True, (255, 255, 255))
        highscore_text = self.font.render(f'{self.score}', True, (255, 255, 255))
        self.screen.blit(self.highscore_asset, (450, 400))
        self.screen.blit(score_text, (750, 405))
        self.screen.blit(self.sua_score_texto, (450, 500))
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
                        nome_do_jogo = menu.main(self.score)
                        return nome_do_jogo
                    elif self.botao_sair.get_rect(topleft=(625, 250)).collidepoint(x,y):
                        sys.exit()

            self.screen.fill((4, 3, 45))
            self.screen.blit(self.gameover_text, (300, 100))
            self.screen.blit(self.botao_menu, (375, 250))
            self.screen.blit(self.botao_sair, (625, 250))
            self.draw_score()
            pygame.display.flip()
