
class Status_jogo():
    '''Armazena dados estatisticos'''
    def __init__(self,ai_configurações):
        '''Inicializa os dados estatisticos'''
        self.ai_configurações = ai_configurações
        self.resetar_status()
        self.jogo_ativo = False
        self.pontuação_maxima = 0

    def resetar_status(self):
        '''Inicializa os dados estatisticos que podem ser mudados durante o jogo'''
        self.espaçonaves_restantes = self.ai_configurações.limite_espaçonaves
        self.pontuação = 0
        self.level = 1