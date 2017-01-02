import pygame

#Cores
branco = (255, 255, 255)
verde = (51, 204, 51)

forca_pulo = -5

class Bird(object):
    def __init__(self):
        self.largura = 20
        self.altura = 20
        self.x = 290
        self.y = 190
        self.velocidade = -6
        self.corpo = pygame.Rect(self.x, self.y , self.largura, self.altura)

    def cair(self, gravidade):
        self.velocidade += gravidade
        self.corpo.move_ip(0, self.velocidade)

    def pula(self):
        self.velocidade = 0
        self.velocidade += forca_pulo

    def desenha(self, tela):
        pygame.draw.rect(tela, verde, self.corpo)
        pygame.draw.rect
