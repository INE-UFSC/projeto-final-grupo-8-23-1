class Position:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def change_x(self, value: int):
        self.__x += value

    def change_y(self, value: int):
        self.__y += value


class Sprite:
    def __init__(self):
        pass


class Entity:
    def __init__(self, position: Position, velocidade: int,
                 tamanho: (int, int), sprite: Sprite,
                 vidas: int, velocidade_v: int, gravidade: int):
        self.__position = position
        self.__velocidade = velocidade
        self.__velocidade_v = velocidade_v
        self.__sprite = sprite
        self.__vidas = vidas
        self.__gravidade = gravidade

    def checar_colisao(self, entidade):
        pass

    def mudar_posicao(self, speed: (int, int)):
        self.__position.change_x(speed[0])
        self.__position.change_y(speed[1])

    def morrer(self):
        del self


class AbstractEnemy(Entity):
    def atacar():
        pass


class InimigoAmbulante(AbstractEnemy):
    def __init__(self, position: Position, velocidade: int,
                 tamanho: (int, int), sprite: Sprite,
                 vidas: int, gravidade: int):
        super().__init__(position, velocidade, tamanho, sprite, vidas,
                         0, gravidade)

    def mudar_posicao(self):
        super().mudar_posicao((self.velocidade, 0))


class InimigoSaltitante(AbstractEnemy):
    def __init__(self, position: Position, velocidade: int, velocidade_v: int,
                 tamanho: (int, int), sprite: Sprite, vidas: int,
                 gravidade: int):
        super().__init__(position, velocidade, tamanho, sprite,
                         vidas, velocidade_v, gravidade)

    def mudar_posicao(self):
        super().mudar_posicao((self.velocidade, 0))

    def saltar(self):
        super().mudar_posicao((0, self.velocidade_v))


class Player(Entity):
    def __init__(self, position: Position, velocidade: int, velocidade_v: int,
                 tamanho: (int, int), sprite: Sprite, vidas: int, estado: str,
                 tiro_pronto: int, direcao: int, gravidade: int):
        super().__init__(position, velocidade, tamanho, sprite,
                         vidas, velocidade_v, gravidade)
        self.__estado = estado
        self.__tiro_pronto = tiro_pronto
        self.direcao = direcao

    def mudar_direcao(self, value):
        self.__direcao = value

    def receber_dano(self):
        self.vidas -= 1

    def atacar(self):
        self.tiro_pronto = 10
        # Spawnar tiro


class Tiro(Entity):
    def __init__(self, position: Position, velocidade: int, velocidade_v: int,
                 tamanho: (int, int), sprite: Sprite, direcao: int,
                 gravidade: int):
        super().__init__(position, velocidade, tamanho, sprite,
                         0, velocidade_v, gravidade)

    def checar_saida(limite_x: int, limite_y: int):
        # Se fora da tela se deletar
        pass

