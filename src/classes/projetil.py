from .gameobject import GameObject, globals
import pygame
import math

bullet_speed = 10
bullet_radius = 5  # tamanho bullets
RED = (255, 0, 0)


class Projetil(GameObject):
    def __init__(self, x, y, angle):
        super().__init__("projetil")
        self.x = x
        self.y = y
        self.dx = math.cos(angle) * bullet_speed
        self.dy = math.sin(angle) * bullet_speed

    def update(self, events):
        self.x += self.dx
        self.y += self.dy
        if (
            self.x < -bullet_radius
            or self.x > globals.var.screen_size.x + bullet_radius
        ):
            self.__del__()
        else:
            # obtem uma lista de todos os inimigos
            inimigos = GameObject.find("inimigo")
            for enemy in inimigos:
                # verifica se o projetil colidiu com o inimigo
                if (
                    math.sqrt((self.x - enemy.pos.x) ** 2 + (self.y - enemy.pos.y) ** 2)
                    < enemy.radius + bullet_radius
                ):
                    self.__del__()  # remover bullet colidido
                    enemy.health -= 1  # diminui hp do inimigo atingido
                    if (
                        enemy.health <= 0
                    ):  # se a vida do inimigo for 0 ou menos, ele eh deletado
                        enemy.__del__()  # remove o inimigo da lista
                    break

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), bullet_radius)
