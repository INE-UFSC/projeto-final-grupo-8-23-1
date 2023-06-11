import pygame
from controlador import Controlador
from menu import Menu

pygame.init()

screen = pygame.display.set_mode((1400, 800))
controlador = Controlador(screen)
menu = Menu(screen)

menu.main(controlador)
controlador.run()
