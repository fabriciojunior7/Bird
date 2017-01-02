import pygame, random

#Cores
branco = (255, 255, 255)
amarelo = (255, 255, 0)

class Nuvem(object):
    def __init__(self):
        self.largura = random.randint(20, 70)
        self.altura = random.randint(5, 25)
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 100)
        self.velocidade = random.randint(1, 30) / 100.0
        self.corpo = pygame.Surface((self.largura, self.altura))


    def desenha(self, tela):
        self.corpo.fill(branco)
        tela.blit(self.corpo, (self.x, self.y))

    def anda(self):
        self.x -= self.velocidade

    def volta(self):
        self.largura = random.randint(20, 70)
        self.altura = random.randint(5, 25)
        self.x = 600
        self.y = random.randint(0, 100)
        self.velocidade = random.randint(1, 30) / 100.0
        self.corpo = pygame.Surface((self.largura, self.altura))

class Sol(object):
    def desenha(self, tela):
        self = pygame.draw.circle(tela, amarelo, (550, 50), 40)
