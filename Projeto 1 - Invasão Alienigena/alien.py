import os
import pygame
from pygame.sprite import Sprite

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Alienigena(Sprite):
    '''uma classe que representa um alienigena'''
    
    def __init__(self,ai_configurações,screen):
        '''Inicializa o alienigena na posição inicial'''
        super(Alienigena,self).__init__()
        self.screen = screen
        self.ai_configurações = ai_configurações
        self.image = pygame.image.load('imagens/alien.bmp')
        self.rect = self.image.get_rect()


        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        '''Desenha o alienigena na sua posição atual'''
        self.screen.blit(self.image,self.rect)

    def checar_bordas(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_configurações.alienigena_velocidade * self.ai_configurações.direção_frota)
        self.rect.x = self.x
