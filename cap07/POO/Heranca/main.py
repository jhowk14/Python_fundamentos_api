from classe import *
animal=Animal('preto', '10kg')
cachorro=Cachorro('caramelo', '15kg')
passaro=Passaro('vermelho', '200g', 'curto')
papagaio=Papagaio('verde/amarelo', '500g', 'redondo')

print('Animal')
print(animal.cor, animal.peso)
animal.dormir()
print('---')

print('Cachorro')
print(cachorro.cor, cachorro.peso, cachorro.rabo)
cachorro.dormir()
cachorro.latir()
print('---')

print('Passaro')
print(passaro.cor, passaro.peso, passaro.bico)
passaro.dormir()
passaro.voar()
print('---')

print('Papagaio')
print(papagaio.cor, papagaio.peso, papagaio.sabeFalar)
papagaio.dormir()
papagaio.voar()
papagaio.falar()
print('---')

