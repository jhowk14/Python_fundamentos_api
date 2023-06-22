class Animal:  
    def __init__(self, cor, peso):
        self.cor=cor
        self.peso=peso
    def dormir(self):
        print('Dormirmindo...')

class Passaro(Animal):
    def __init__(self, cor, peso, bico):
        super().__init__(cor, peso)
        self.bico=bico
    def voar(self):
        print('Voando...')
        
class Papagaio(Passaro):
    def __init__(self, cor, peso, bico):
        super().__init__(cor, peso, bico)
        self.sabeFalar=True
    def falar(self):
        print('Falando...')
        
class Cachorro(Animal):
    def __init__(self, cor, peso):
        super().__init__(cor, peso)
        self.rabo=True
    def latir(self):
        print('Latindo...')
        
        
    