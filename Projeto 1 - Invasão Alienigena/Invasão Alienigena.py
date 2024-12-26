'''Projeto 1 - Invasão Alienigena'''

import pygame
import os
from configurações import Configurações
from espaçonave import Espaçonave
import funções_jogo as fj
from pygame.sprite import Group
from status_jogo import Status_jogo
from botão import Botão
from pontuação import Pontuação

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def rodar_jogo():
    '''Inicializa o jogo e cria um objeto para a tela'''
    pygame.init()
    clock = pygame.time.Clock()
    ai_configurações = Configurações()
    screen = pygame.display.set_mode((ai_configurações.largura_tela,ai_configurações.altura_tela))
    pygame.display.set_caption("Invasão Alienigena")
    botao_jogar = Botão(ai_configurações,screen,"Jogar")
    status = Status_jogo(ai_configurações)
    po = Pontuação(ai_configurações,screen,status)
    '''Cria uma espaçonave'''
    espaçonave = Espaçonave(screen,ai_configurações)
 
    '''Cria um grupo para armazenar a bala'''
    balas = Group()
    alienigenas = Group()
    fj.criar_frota(ai_configurações,screen,espaçonave,alienigenas)
    '''Inicia o laço principal do jogo'''
    while True:
        fj.checar_eventos(ai_configurações,screen,status,po,botao_jogar,espaçonave,alienigenas,balas)
        
        if status.jogo_ativo: 
            espaçonave.atualizar()
            fj.atualizar_balas(ai_configurações,screen,status,po,espaçonave,alienigenas,balas)
            fj.atualizar_alienigenas(ai_configurações,status,screen,po,espaçonave,alienigenas,balas)
        
        fj.atualizar_tela(ai_configurações,screen,status,po,espaçonave,alienigenas,balas,botao_jogar)
        

        clock.tick(60)

rodar_jogo()
