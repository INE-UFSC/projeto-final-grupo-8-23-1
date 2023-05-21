import pygame


class Hud:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 36)
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000
        timer_text = self.font.render("Tempo: " + str(seconds), True, (255, 255, 255))
        self.game.screen.blit(timer_text, (620, 10))

        lives_text = self.font.render("Vidas: ", True, (255, 255, 255))
        self.game.screen.blit(lives_text, (20, 10))

        lives_text = self.font.render(str(self.game.player.lives), True, (255, 0, 0))
        self.game.screen.blit(lives_text, (100, 10))
