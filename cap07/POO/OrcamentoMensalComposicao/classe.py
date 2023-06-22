class CicloMensal:
    def __init__(self, mes, ano):
        self.mes=mes
        self.ano=ano
        self.lancamentos=[]
    def addLancamento(self,descricao, valor):
        lancamento=Lancamento(descricao, valor)
        self.lancamentos.append(lancamento)
    
    def calcularTotal(self):
        total=0
        for l in self.lancamentos:
            print(f'{l.descricao} | R${l.valor:.2f}')
            total+=l.valor
        return total
                
class Lancamento:  
    def __init__(self, descricao, valor):
        self.descricao=descricao
        self.valor=valor
