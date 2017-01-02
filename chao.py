import pygame

#Cores
mostarda = (179, 179, 0)

class Chao(object):
    def __init__(self, largura_tela):
        self.largura = largura_tela
        self.altura = 20
        self.x = 0
        self.y = 380
        self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenha(self, tela):
        pygame.draw.rect(tela, mostarda, self.corpo)