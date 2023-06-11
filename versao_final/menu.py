import pygame
from pygame.locals import *


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.logo = pygame.image.load('assets/logo.png')
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.center = (400, 100)

        self.buttons = {
            'Mario': pygame.image.load('assets/botao_mario.png'),
            'Shooter': pygame.image.load('assets/botao_shooter.png'),
            'Pong': pygame.image.load('assets/botao_pong.png'),
            'Bricks': pygame.image.load('assets/botao_bricks.png')
        }
        self.button_rects = {
            name: img.get_rect() for name, img in self.buttons.items()
        }

        # Place the buttons side by side
        for i, rect in enumerate(self.button_rects.values()):
            rect.center = (200 * (i + 1), 300)

        self.footer = pygame.image.load('assets/nomes.png')
        self.footer_rect = self.footer.get_rect()
        self.footer_rect.center = (400, 550)

    def draw(self):
        self.screen.fill((4, 3, 35))
        self.screen.blit(self.logo, self.logo_rect.topleft)  # Desenha a logo
        for img, rect in zip(self.buttons.values(), self.button_rects.values()):
            self.screen.blit(img, rect.topleft)  # Desenha os botoes
        self.screen.blit(self.footer, self.footer_rect.topleft)  # Desenha os nomes

    def check_click(self, pos):
        for name, rect in self.button_rects.items():
            if rect.collidepoint(pos):
                return name  # Retorna o nome do Botao apertado
        return None

    def main(self, controlador):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    button = self.check_click(event.pos)
                    if button is not None:
                        controlador.set_jogo(button)
                        controlador.run()
                        return

            self.draw()
            pygame.display.flip()
            clock.tick(60)
