import pygame
import os
from pygame.sprite import Sprite

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Espaçonave(Sprite):
    def __init__(self,screen,ai_configurações):
        '''Inicializa a espaçonave e define sua posição inicial'''
        super(Espaçonave,self).__init__()
        self.screen = screen
        self.ai_configurações = ai_configurações
        #Carrega a image da espaçonave e obtem o seu desenho
        self.image = pygame.image.load('imagens/espaçonave.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Inicia cada nova espaçonave na parte inferior central da screen
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom

        #Armazena um valor decimal para o centro da espaçonave
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #Flag de movimento
        self.movendo_direita = False
        self.movendo_esquerda = False
        self.movendo_cima = False
        self.movendo_baixo = False


    def atualizar(self):
        '''Atualiza a posição da espaçonave de acordo com a flag de movimento'''
        if self.movendo_direita and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_configurações.velocidade_espaçonave

        elif self.movendo_esquerda and self.rect.left > 0:
            self.centerx -= self.ai_configurações.velocidade_espaçonave
        if self.movendo_cima and self.rect.top >0:
            self.centery -= 1
        elif self.movendo_baixo and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 1 
        
        #Atualiza o objeto rect(espaçonave) de acordo com o self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        '''Desenha a espaçonave em sua posição atual'''
        self.screen.blit(self.image,self.rect)

    def centralizar_espaçonave(self):
        self.rect.centerx = self.screen_rect.centerx   
        self.x = float(self.rect.centerx)