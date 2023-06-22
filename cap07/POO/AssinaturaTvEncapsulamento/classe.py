class AssinaturaTv:  
    def __init__(self):
        self.canaisDisponiveis=(2, 5, 7, 15, 30, 50)
        self.__canalAtivo = 7
        self.volume=10
    @property
    def canalAtivo(self):
        return(self.__canalAtivo)
    @canalAtivo.setter
    def canalAtivo(self, canal):
        try:
            index=self.canaisDisponiveis.index(canal)
            self.__canalAtivo=canal
            print(f'O canal ativo agora é: {canal}')
        except:
            index=-1
            print(f'O canal {canal} não está disponível')
            
            