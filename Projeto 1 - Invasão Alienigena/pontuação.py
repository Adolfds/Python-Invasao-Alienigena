import pygame.font
from pygame.sprite import Group
from espaçonave import Espaçonave

class Pontuação():
    '''informações sobre a pontuação'''

    def __init__(self,ai_configurações,screen,status):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_configurações = ai_configurações
        self.status = status

        #Configurações da fonte da pontuação
        self.cor_texto = (30,30,30)
        self.fonte = pygame.font.SysFont(None,48)

        #Prepara a imagem da pontuação inicial
        self.prep_ponto()
        self.prep_pontuação_maxima()
        self.prep_level()
        self.prep_espaçonaves()

    def prep_ponto(self):
        ponto_arredondado = int(round(self.status.pontuação, -1))
        ponto_str = "{:,}".format(ponto_arredondado)
        self.ponto_imagem = self.fonte.render(ponto_str,True,self.cor_texto,self.ai_configurações.cor_fundo)

        self.ponto_rect = self.ponto_imagem.get_rect()
        self.ponto_rect.right = self.screen_rect.right - 20
        self.ponto_rect.top = 20
    
    def prep_pontuação_maxima(self):
        pontuação_maxima = int(round(self.status.pontuação_maxima, -1))
        pontuação_maxima_str = "{:,}".format(pontuação_maxima)
        self.pontuaçao_maxima_imagem = self.fonte.render(pontuação_maxima_str,True,self.cor_texto,self.ai_configurações.cor_fundo)
        self.pontuação_maxima_rect = self.pontuaçao_maxima_imagem.get_rect()
        self.pontuação_maxima_rect.centerx = self.screen_rect.centerx
        self.pontuação_maxima_rect.top = self.ponto_rect.top

    def prep_level(self):
        self.level_imagem = self.fonte.render(str(self.status.level),True,self.cor_texto,self.ai_configurações.cor_fundo)
        self.level_rect = self.level_imagem.get_rect()
        self.level_rect.right = self.ponto_rect.right
        self.level_rect.top = self.ponto_rect.bottom + 10

    def prep_espaçonaves(self):
        '''Mostra quantas espaçonaves restam de vida'''
        self.espaçonaves = Group()
        for numero_espaçonaves in range(self.status.espaçonaves_restantes):
            espaçonave = Espaçonave(self.screen,self.ai_configurações)
            espaçonave.rect.x = 10 + numero_espaçonaves * espaçonave.rect.width
            espaçonave.rect.y = 10
            self.espaçonaves.add(espaçonave)

    def mostrar_ponto(self): 
        self.screen.blit(self.ponto_imagem,self.ponto_rect)
        self.screen.blit(self.pontuaçao_maxima_imagem,self.pontuação_maxima_rect)
        self.screen.blit(self.level_imagem,self.level_rect)
        self.espaçonaves.draw(self.screen)