from classe import *
abril=CicloMensal( 'Abril', 22)
abril.addLancamento('Salario', 4000)
abril.addLancamento('Cartão Alimentação', 600)
abril.addLancamento('Trabalho Extra', 2000)
abril.addLancamento('Supermercado', -2000)
abril.addLancamento('Cartão de creditos', -1800)
print('-----')
print(f'Lançamentos: {abril.mes}/{abril.ano}')
print('---')
total=abril.calcularTotal()
print('---')
print(f'Total: R${total}')




