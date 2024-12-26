import pygame.font

class Botão():
    def __init__(self,ai_configurações,screen,msg):
        '''Inicializa os atributos do botão'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #As dimensoes e propriedades do botão
        self.largura,self.altura = 200,50
        self.cor_botão = (255,0,0)
        self.cor_texto = (255,255,255)
        self.fonte = pygame.font.SysFont(None,48)
        #Constroi o botão e o centraliza
        self.rect = pygame.Rect(0,0,self.largura,self.altura)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self,msg):
        '''Transforma msg em imagem renderizada e centraliza o texto no botao'''
        self.msg_imagem = self.fonte.render(msg,True,self.cor_texto,self.cor_botão)
        self.msg_image_rect = self.msg_imagem.get_rect()
        self.msg_image_rect.center = self.rect.center

    def desenhar_botao(self):
        '''Desenha o botao em branco e a mensagem'''
        self.screen.fill(self.cor_botão,self.rect)
        self.screen.blit(self.msg_imagem,self.msg_image_rect)
