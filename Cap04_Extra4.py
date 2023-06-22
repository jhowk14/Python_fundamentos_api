from os import system, name
system('cls') if (name=='nt') else system('clear')
print('------------Promoções------------')
print('')

linha = 1

produto = 'Notebook'
precoCusto = 1800
precoVenda = 3000
desconto = 100
dia = 0

while precoVenda > precoCusto:
    dia+=1
    print(f'{dia}o. Dia - Preco R$ {precoVenda:2}')
    precoVenda -= desconto
    
print(f'{dia}o. Dia - Preco minimo atingido ...')