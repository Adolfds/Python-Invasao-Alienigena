
class Configurações():
    '''Uma classe para armazenar todas as configurações de Invasão Alienigena'''
    def __init__(self):
        '''Inicializa as configurações do jogo'''
        #Configurações de tela
        self.largura_tela = 1280
        self.altura_tela = 800
        self.cor_fundo = (230,230,230)
        #Configurações da frota alienigena
        self.descida_frota = 10

        #Configurações das balas da nave
        self.bala_largura = 3
        self.bala_altura = 15
        self.cor_bala = 60,60,60
        self.balas_permitidas = 3

        #Configurações da espaçonave
        self.limite_espaçonaves = 3

        #Velocidade para o jogo aumentar
        self.velocidade_aumento = 1.5

        #Aumentar a pontuação para cada nivel
        self.aumento_pontuação = 1.5

        self.iniciar_configurações_dinamicas()

    def iniciar_configurações_dinamicas(self):
        self.velocidade_espaçonave = 3
        self.velocidade_bala = 3
        self.alienigena_velocidade = 1
        self.direção_frota = 1
        self.pontos_alienigenas = 50

    def aumentar_velocidade(self):
        self.velocidade_espaçonave *= self.velocidade_aumento
        self.velocidade_bala *= self.velocidade_aumento
        self.alienigena_velocidade *= self.velocidade_aumento
        self.pontos_alienigenas = int(self.pontos_alienigenas * self.aumento_pontuação)