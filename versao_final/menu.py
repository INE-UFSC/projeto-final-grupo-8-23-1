import pygame
from pygame.locals import *
from highscore import Highscore


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('assets/assets_menu/tela_de_fundo_menu.png')
        self.highscore_icon = pygame.image.load('assets/assets_menu/highscore.png')
        self.start_button = pygame.image.load('assets/assets_menu/botao_jogar.png')
        self.quit_button = pygame.image.load('assets/assets_menu/botao_tutorial.png')
        self.selection_icon1 = pygame.image.load('assets/assets_menu/selecionador.png')
        self.selection_icon2 = pygame.image.load('assets/assets_menu/selecionador2.png')
        self.buttons = [self.start_button, self.quit_button]
        self.current_selection = 0
        self.button_positions = [(510, 225), (595, 418)]
        self.selection_positions = [(500, 240), (582, 422)]
        self.highscore = Highscore()
        self.font = pygame.font.SysFont('bahnschrift', 26)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.highscore_icon, (205, 375))
        highscore_text = self.font.render(str(self.highscore.highscore), True, (255, 215, 0))
        self.screen.blit(highscore_text, (245, 410))
        for i, button in enumerate(self.buttons):
            self.screen.blit(button, self.button_positions[i])
            if i == self.current_selection:
                if self.current_selection == 0:
                    self.screen.blit(self.selection_icon1, self.selection_positions[i])
                elif self.current_selection == 1:
                    self.screen.blit(self.selection_icon2, self.selection_positions[i])
        pygame.display.flip()

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.current_selection = (self.current_selection - 1) % len(self.buttons)
                    elif event.key == pygame.K_s:
                        self.current_selection = (self.current_selection + 1) % len(self.buttons)
                    elif event.key == pygame.K_SPACE:
                        if self.current_selection == 0:
                            return 'start'
                        elif self.current_selection == 1:
                            pygame.quit()
                            return
            self.draw()
