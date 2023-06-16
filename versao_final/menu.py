import pygame
from pygame.locals import *


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.logo = pygame.image.load('./assets/logo2.png')
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.center = (600, 100)

        self.highscore_font = pygame.font.SysFont('bahnschrift', 45)
        self.highscore_asset = pygame.image.load('./assets/highscore2.png')
        self.highscore_asset_rect = self.highscore_asset.get_rect()
        self.highscore_asset_rect.center = (600, 200)

        self.buttons = {
            'Mario': pygame.image.load('./assets/botao_mario.png'),
            'Shooter': pygame.image.load('./assets/botao_shooter.png'),
            'Flappy': pygame.image.load('./assets/botao_pong.png'),
            'Bricks': pygame.image.load('./assets/botao_bricks.png'),
            # Add your four new buttons here
            'NewButton1': pygame.image.load('./assets/botao_bricks2.png'),
            'NewButton2': pygame.image.load('./assets/botao_bricks2.png'),
            'NewButton3': pygame.image.load('./assets/botao_bricks2.png'),
            'NewButton4': pygame.image.load('./assets/botao_bricks2.png')
        }

        self.button_rects = {
            name: img.get_rect() for name, img in self.buttons.items()
        }

        for i, rect in enumerate(self.button_rects.values()):
            if i < 4:
                rect.center = (300 * (i + 0.5), 350)
            else:
                rect.center = (300 * ((i - 4) + 0.5), 450)

        self.footer = pygame.image.load('./assets/nomes.png')
        self.footer_rect = self.footer.get_rect()
        self.footer_rect.center = (450, 680)

    def draw(self):
        self.screen.fill((4, 3, 35))
        self.screen.blit(self.logo, self.logo_rect.topleft)

        self.screen.blit(self.highscore_asset, self.highscore_asset_rect.topleft)
        highscore_surface = self.highscore_font.render('00', True, (255, 215, 0))
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

    def main(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    button = self.check_click(event.pos)
                    if button is not None:
                        return button

            self.draw()
            pygame.display.flip()
            clock.tick(60)
