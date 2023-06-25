import pygame
from pygame.locals import *


class Menu:
    def __init__(self, screen):
        self.screen = screen
<<<<<<< HEAD
        self.background = pygame.image.load('assets/assets_menu/tela_de_fundo_menu.png')
        self.highscore_icon = pygame.image.load('assets/assets_menu/highscore.png')
        self.start_button = pygame.image.load('assets/assets_menu/botao_jogar.png')
        self.quit_button = pygame.image.load('assets/assets_menu/botao_tutorial.png')
        self.selection_icon = pygame.image.load('assets/assets_menu/selecionador.png')
        self.buttons = [self.start_button, self.quit_button]
        self.current_selection = 0
        self.button_positions = [(510, 225), (595, 418)]
        self.selection_positions = [(500, 240), (580, 418)]

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.highscore_icon, (205, 375))
        for i, button in enumerate(self.buttons):
            self.screen.blit(button, self.button_positions[i])
            if i == self.current_selection:
                self.screen.blit(self.selection_icon, self.selection_positions[i])
        pygame.display.flip()

    def main(self):
        running = True
        while running:
=======
        self.logo = pygame.image.load('versao_final/assets/logo2.png')
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.center = (600, 100)

        self.highscore_font = pygame.font.SysFont('bahnschrift', 45)
        self.highscore_asset = pygame.image.load('versao_final/assets/highscore2.png')
        self.highscore_asset_rect = self.highscore_asset.get_rect()
        self.highscore_asset_rect.center = (600, 200)

        self.buttons = {
            'Mario': pygame.image.load('versao_final/assets/botao_mario.png'),
            'Shooter': pygame.image.load('versao_final/assets/botao_shooter.png'),
            'Flappy': pygame.image.load('versao_final/assets/botao_flappy.png'),
            'Asteroid': pygame.image.load('versao_final/assets/botao_bricks.png'),
            # Add your four new buttons here
            'NewButton1': pygame.image.load('versao_final/assets/botao_bricks2.png'),
            'NewButton2': pygame.image.load('versao_final/assets/botao_bricks2.png'),
            'NewButton3': pygame.image.load('versao_final/assets/botao_bricks2.png'),
            'NewButton4': pygame.image.load('versao_final/assets/botao_bricks2.png')
        }

        self.button_rects = {
            name: img.get_rect() for name, img in self.buttons.items()
        }

        for i, rect in enumerate(self.button_rects.values()):
            if i < 4:
                rect.center = (300 * (i + 0.5), 350)
            else:
                rect.center = (300 * ((i - 4) + 0.5), 450)

        self.footer = pygame.image.load('versao_final/assets/nomes.png')
        self.footer_rect = self.footer.get_rect()
        self.footer_rect.center = (450, 680)

    def draw(self, score):
        self.screen.fill((4, 3, 35))
        self.screen.blit(self.logo, self.logo_rect.topleft)

        self.screen.blit(self.highscore_asset, self.highscore_asset_rect.topleft)
        highscore_surface = self.highscore_font.render(str(score), True, (255, 215, 0))
        highscore_rect = highscore_surface.get_rect(midleft=(self.highscore_asset_rect.right + 20, 200))
        self.screen.blit(highscore_surface, highscore_rect)

        for img, rect in zip(self.buttons.values(), self.button_rects.values()):
            self.screen.blit(img, rect.topleft)

        self.screen.blit(self.footer, self.footer_rect.topleft)

    def check_click(self, pos):
        for name, rect in self.button_rects.items():
            if rect.collidepoint(pos):
                return name  # Retorna o nome do botao apertado
        return None

    def main(self, score):
        clock = pygame.time.Clock()
        while True:
>>>>>>> a6199b2fc287f4f0ff78ea808f75f6e5b7aea1a4
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
                        if self.current_selection == 0:  # start
                            return 'start'
                        elif self.current_selection == 1:  # quit
                            pygame.quit()
                            return
            self.draw()
