import pygame


class Hud:
    def __init__(self, controlador):
        self.controlador = controlador
        self.font = pygame.font.SysFont('bahnschrift', 35)

        self.vida_icon = pygame.image.load('assets/vida.png')
        self.troca_mundo_icon = pygame.image.load('assets/troca_de_mundo_texto.png')
        self.tempo_texto_icon = pygame.image.load('assets/tempo_texto.png')
       # self.score_texto_icon = pygame.image.load('assets/tempo_texto.png')
        self.barra_vertical_icon = pygame.image.load('assets/linha_vertical.png')

    def draw(self, screen):
        # Desenhar o número de vidas
        for i in range(self.controlador.player.get_vidas()):
            screen.blit(self.vida_icon, (10 + i * (self.vida_icon.get_width() + 10), 10))
        vidas_text = self.font.render(str(self.controlador.vidas), True, (255, 255, 255))

        # Desenhar o tempo restante para a troca de mundo
        screen.blit(self.troca_mundo_icon, (300, 20))
        tempo_troca_mundo = max(0, (self.controlador.tempo_troca_de_fase - self.controlador.tempo_na_fase) // 1000) +1
        tempo_troca_text = self.font.render(str(tempo_troca_mundo), True, (255, 255, 255))
        screen.blit(tempo_troca_text, (600, 20))

        # Desenhar o tempo total decorrido
        screen.blit(self.tempo_texto_icon, (700, 20))
        tempo_total_text = self.font.render(str(self.controlador.tempo // 1000), True, (255, 255, 255))
        screen.blit(tempo_total_text, (900, 20))

        # Desenhar a pontuação
        #screen.blit(self.score_texto_icon, (280, 10))
        #score_text = self.font.render(str(self.controlador.pontuacao), True, (255, 255, 255))
        #screen.blit(score_text, (320, 10))

        pygame.display.flip()

    def update(self):
        pass  # Neste caso, nada precisa ser atualizado
