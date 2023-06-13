import pygame
from controlador import Controlador
from menu import Menu

pygame.init()
screen = pygame.display.set_mode((1200, 700))
controlador = Controlador(screen)
controlador.run()
