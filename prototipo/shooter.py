import pygame
from jogoabstrato import JogoAbstrato

class Shooter(JogoAbstrato):
    def __init__(self, entidades):
        self.entidades = entidades
    
    def adicionar_entidade(self):
        #adicionar_entidades
        pass

    def remover_entidade(self):
        #remover_entidades
        pass

    def lidar_fisica(self):
        #lidar_fisica
        pass

    def checar_colisao(self):
        #checar_colisao
        pass

    def update(self, tempo, tempo_na_fase, num_fases):
        print(f"Jogo: Shooter / Tempo: {tempo} / Tempo na fase: {tempo_na_fase} / Fase: {num_fases}")
