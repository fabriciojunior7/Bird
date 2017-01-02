import pygame, random

#Cores
preto = (0, 0, 0)
azul = (0, 0, 255)

class Tubos(object):
    def __init__(self, x):
        #self.largura = random.randint(10, 50)
        self.largura = 20
        self.altura = 500
        self.x = x
        self.y = 300
        self.velocidade = 1
        self.corpo = pygame.Rect(self.x, self.y , self.largura, self.altura)
        self.moeda = pygame.Rect((self.x + 9), 0 , 2, 600)

    def desenha(self, tela):
        pygame.draw.rect(tela, preto, self.corpo)
        #pygame.draw.rect(tela, azul, self.moeda)

    def anda(self):
        self.corpo.x -= self.velocidade
        self.moeda.x -= self.velocidade

    def volta(self, y):
        self.x = 600
        self.y = y
        self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.moeda = pygame.Rect((self.x + 9), 0, 2, 600)