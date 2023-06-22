import os
os.system('cls'if os.name=='nt'else 'clear')

print('Vamos calcular a raiz quadrada')
n = input('informe o número: ')
print('O valor é um número inteiro? ' , n.isnumeric())
print('O valor é um número com casas decimais? ' , n.isdecimal())
# ** =  Exponenciação - retorna um número elevado a potência de outro, para raiz quadrada use 1/2
resultado = int(n) ** (1/2)
print('A raiz quadrada de {} é {:.2f}'.format(n, resultado))
