import sys
import pygame
from bala import Bala
from alien import Alienigena
from time import sleep

def checar_eventos(ai_configurações,screen,status,po,botao_jogar,espaçonave,alienigenas,balas):
    '''Observa os eventos de teclado e mouse'''
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            checar_pressionamento_teclas(evento,ai_configurações,screen,status,espaçonave,alienigenas,balas)
        elif evento.type == pygame.KEYUP:
            checar_soltar_teclas(evento,espaçonave)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            checar_botao_jogar(ai_configurações,screen,status,po,botao_jogar,espaçonave,alienigenas,balas,mouse_x,mouse_y)

def checar_botao_jogar(ai_configurações,screen,status,po,botao_jogar,espaçonave,alienigenas,balas,mouse_x,mouse_y):
    '''Inicia um novo jogo quando clicado em play'''
    botao_clicado = botao_jogar.rect.collidepoint(mouse_x,mouse_y)
    if botao_clicado and not status.jogo_ativo:
        ai_configurações.iniciar_configurações_dinamicas()
        pygame.mouse.set_visible(False)
        status.resetar_status()
        status.jogo_ativo = True
        po.prep_ponto()
        po.prep_pontuação_maxima()
        po.prep_level()
        po.prep_espaçonaves()
        alienigenas.empty()
        balas.empty()
        criar_frota(ai_configurações,screen,espaçonave,alienigenas)
        espaçonave.centralizar_espaçonave()

def checar_pressionamento_teclas(evento,ai_configurações,screen,status,espaçonave,alienigenas,balas):
    '''Verifica o pressionamentos de tecla'''
    #Move a espaçonave para a direita
    if evento.key == pygame.K_RIGHT:
        espaçonave.movendo_direita = True
    #Move a espaçonave para a esquerda
    elif evento.key == pygame.K_LEFT:
        espaçonave.movendo_esquerda = True
    elif evento.key == pygame.K_SPACE:
        atirar_balas(ai_configurações,screen,espaçonave,balas)
    elif evento.key == pygame.K_p:
        if not status.jogo_ativo:
            ai_configurações.iniciar_configurações_dinamicas()
            pygame.mouse.set_visible(False) 
            status.resetar_status() 
            status.jogo_ativo = True 
            alienigenas.empty() 
            balas.empty() 
            criar_frota(ai_configurações, screen, espaçonave, alienigenas)
    elif evento.key == pygame.K_q:
        sys.exit()

def espaçonave_acertada(ai_configurações,screen,status,po,espaçonave,alienigenas,balas):
    '''mostra quando a espaçonave é acertada por alienigena'''
    if status.espaçonaves_restantes > 0:
        status.espaçonaves_restantes -= 1
        po.prep_espaçonaves()
        alienigenas.empty()
        balas.empty()
        criar_frota(ai_configurações,screen,espaçonave,alienigenas)
        espaçonave.centralizar_espaçonave()
        sleep(0.5)
    else:
        status.jogo_ativo = False
        pygame.mouse.set_visible(True)

def atirar_balas(ai_configurações,screen,espaçonave,balas):
    if len(balas) < ai_configurações.balas_permitidas:
            nova_bala = Bala(ai_configurações,screen,espaçonave)
            balas.add(nova_bala)

def atualizar_balas(ai_configurações,screen,status,po,espaçonave,alienigenas,balas):
    '''Atualiza a posição das balas e se livra das antigas'''
    balas.update()
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)
    checar_colisao_bala_alienigena(ai_configurações,screen,status,po,espaçonave,alienigenas,balas)

def checar_colisao_bala_alienigena(ai_configurações,screen,status,po,espaçonave,alienigenas,balas):
    colisoes = pygame.sprite.groupcollide(balas,alienigenas,True,True)
    if colisoes:
        for alienigenas in colisoes.values():
            status.pontuação += ai_configurações.pontos_alienigenas * len(alienigenas)
            po.prep_ponto()
            checar_ponto_maximo(status,po)
    if len(alienigenas) == 0:
        balas.empty()
        ai_configurações.aumentar_velocidade()
        status.level += 1
        po.prep_level()
        criar_frota(ai_configurações,screen,espaçonave,alienigenas)


def checar_ponto_maximo(status,po):
    if status.pontuação > status.pontuação_maxima:
        status.pontuação_maxima = status.pontuação
        po.prep_pontuação_maxima()

def checar_soltar_teclas(evento,espaçonave):
    '''Verifica a soltura de teclas'''
    if evento.key == pygame.K_RIGHT:
        espaçonave.movendo_direita = False
    elif evento.key == pygame.K_LEFT:
        espaçonave.movendo_esquerda = False
    elif evento.key == pygame.K_UP:
        espaçonave.movendo_cima = False
    elif evento.key == pygame.K_DOWN:
        espaçonave.movendo_baixo = False

def atualizar_tela(ai_configurações,screen,status,po,espaçonave,alienigenas,balas,botao_jogar):
    '''Redesenha a tela a cada passagem pelo laço'''
    screen.fill(ai_configurações.cor_fundo)
    for bala in balas.sprites():
        bala.desenhar_bala()
    espaçonave.blitme()
    alienigenas.draw(screen)
    po.mostrar_ponto()
    if not status.jogo_ativo:
        botao_jogar.desenhar_botao()

    '''Deixa a tela mais recente visivel'''
    pygame.display.flip()

def pegar_numeros_alienigenas_x(ai_configurações,alienigena_largura):
    espaço_disponivel_x = ai_configurações.largura_tela - 2*alienigena_largura
    numeros_alienigenas_x = int(espaço_disponivel_x/(2*alienigena_largura))
    return numeros_alienigenas_x

def pegar_numero_linhas(ai_configurações,espaçonave_altura,alienigena_altura):
    '''Determina quantos alienigenas cabem pela altura'''
    espaço_disponivel_y = (ai_configurações.altura_tela - (3* alienigena_altura) - espaçonave_altura)
    numero_linhas = int(espaço_disponivel_y / (2* alienigena_altura))
    return numero_linhas

def criar_alienigena(ai_configurações,screen,alienigenas,numero_alienigena,numero_linhas):
    alienigena = Alienigena(ai_configurações,screen)
    alienigena_largura = alienigena.rect.width
    alienigena.x = alienigena_largura + 2 * numero_alienigena * alienigena_largura
    alienigena.rect.x = alienigena.x
    alienigena.rect.y = alienigena.rect.height + 2 * alienigena.rect.height * numero_linhas
    alienigenas.add(alienigena)

def criar_frota(ai_configurações,screen,espaçonave,alienigenas):
    """Cria uma frota completa de alienigenas"""
    alienigena = Alienigena(ai_configurações,screen)
    numero_linhas = pegar_numero_linhas(ai_configurações,espaçonave.rect.height,alienigena.rect.height)
    numeros_alienigenas_x = pegar_numeros_alienigenas_x(ai_configurações,alienigena.rect.width)
    for numero_linha in range(numero_linhas):
        for numero_alienigena in range(numeros_alienigenas_x):
            criar_alienigena(ai_configurações,screen,alienigenas,numero_alienigena,numero_linha)

def checar_borda_frota(ai_configurações,alienigenas):
    for alienigena in alienigenas.sprites():
        if alienigena.checar_bordas():
            mudar_direçao_frota(ai_configurações,alienigenas)
            break

def checar_alienigenas_fundo(ai_configurações,status,screen,espaçonave,alienigenas,balas):
    screen_rect = screen.get_rect()
    for alienigena in alienigenas.sprites():
        if alienigena.rect.bottom >= screen_rect.bottom:
            espaçonave_acertada(ai_configurações,status,screen,espaçonave,alienigenas,balas)
            break


def mudar_direçao_frota(ai_configurações,alienigenas):
    for alienigena in alienigenas.sprites():
        alienigena.rect.y += ai_configurações.descida_frota
    ai_configurações.direção_frota *=-1

def atualizar_alienigenas(ai_configurações,status,screen,po,espaçonave,alienigenas,balas):
    checar_borda_frota(ai_configurações,alienigenas)
    alienigenas.update()
    if pygame.sprite.spritecollideany(espaçonave,alienigenas):
        espaçonave_acertada(ai_configurações,screen,status,po,espaçonave,alienigenas,balas)
    checar_alienigenas_fundo(ai_configurações,status,screen,espaçonave,alienigenas,balas)

