class Sprite:
    def __init__(self):
        pass


class Entidade:
    def __init__(self, posicao_x: int, posicao_y: int, velocidade_x: int, velocidade_y: int,
                 vidas: int, sprite: Sprite, tamanho):
        
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y

        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y

        self.vidas = vidas
        self.sprite = sprite
        self.tamanho = tamanho

    def checar_colisao(self, entidade):
        pass

    def atualizar_posicao(self):

        self.posicao_x += self.velocidade_x
        self.posicao_y += self.velocidade_y

    def morrer(self):
        del self


class Inimigo(Entidade):
    def __init__(self, posicao_x: int, posicao_y: int, velocidade_x: int, velocidade_y: int,
                 vidas: int, sprite: Sprite, tamanho):
        super().__init__(self, posicao_x, posicao_y, velocidade_x, velocidade_y, vidas, sprite, tamanho)


class Jogador(Entidade):

    def __init__(self, posicao_x: int, posicao_y: int, velocidade_x: int, velocidade_y: int,
                 vidas: int, sprite: Sprite, tamanho, estado: str, acoes_prontas: int, direcao: int):
        super().__init__(self, posicao_x, posicao_y, velocidade_x, velocidade_y, vidas, sprite, tamanho)
        
        self.estado = estado
        self.acoes_prontas = acoes_prontas
        self.direcao = direcao

    def mudar_direcao(self, value):
        self.__direcao = value

    def receber_dano(self):
        self.vidas -= 1

    def atacar(self):
        self.tiro_pronto = 10
        # Spawnar tiro

