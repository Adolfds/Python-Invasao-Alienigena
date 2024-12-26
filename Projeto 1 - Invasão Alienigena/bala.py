import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    '''Uma classe que faz a função das balas da nave'''

    def __init__(self,ai_configurações,screen,espaçonave):
        '''Cria um objeto para a bala na posição atual da espaçonave'''
        super(Bala,self).__init__()
        self.screen = screen
        #Cria um retangulo para o projetil em (0,0) e define a posição correta
        self.rect = pygame.Rect(0,0,ai_configurações.bala_largura, ai_configurações.bala_altura)
        self.rect.centerx = espaçonave.rect.centerx
        self.rect.top = espaçonave.rect.top
        #Armazena a bala como float, decimal
        self.y = float(self.rect.y)
        self.cor = ai_configurações.cor_bala
        self.fator_velocidade = ai_configurações.velocidade_bala

    def update(self):
        '''Move a bala para cima'''
        #atualização decimal da bala
        self.y -= self.fator_velocidade
        #Atualiza o rect
        self.rect.y = self.y
    
    def desenhar_bala(self):
        '''Desenha a bala na tela'''
        pygame.draw.rect(self.screen,self.cor,self.rect)
        