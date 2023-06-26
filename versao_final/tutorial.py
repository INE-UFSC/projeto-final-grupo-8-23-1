import pygame


class Tutorial:
    def __init__(self, screen, press_space):
        self.screen = screen
        self.press_space = press_space
        self.background = pygame.image.load('assets/assets_menu/tela_tutorial.png')
        self.press_space_center_position = (600, 630)
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        press_space_image = self.press_space.get_current_frame()
        press_space_position = (self.press_space_center_position[0] - press_space_image.get_width() / 2,
                                self.press_space_center_position[1] - press_space_image.get_height() / 2)
        self.screen.blit(press_space_image, press_space_position)
        pygame.display.flip()

    def main(self):
        running = True
        while running:
            dt = self.clock.tick()
            self.press_space.update(dt)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return
            self.draw()
