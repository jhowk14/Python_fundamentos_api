
from os import system, name
system('cls') if(name == 'nt') else system('clear')

valores=(1500, 850, 825,395.3, 647.2)

#Multiplicar por uma constante
txImposto=0.053
valorImposto = map(lambda item: item*txImposto, valores)
print(list(valorImposto))

#Aplicar máscara
mascaraValoes = map(lambda item: f'R${float(item):.2f}', valores)
print(list(mascaraValoes))

#Aplicando Filtros
filtroValores = filter(lambda item: item>1000, valores)
print(list(filtroValores))
