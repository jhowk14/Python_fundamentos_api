class Produto:  
    def __init__(self, descricao, precoCusto, precoVenda):
        self.descricao=descricao
        self.precoCusto = precoCusto
        self.__precoVenda=precoVenda
    @property
    def precoVenda(self):
        return(self.__precoVenda)
    @precoVenda.setter
    def precoVenda(self, valor):
        if(valor>=self.precoCusto):
            self.__precoVenda=valor
            print(f'Preço de venda alterado para R${valor}')
        else:
            print('O preço de venda não pode ser alterado.')
            
            