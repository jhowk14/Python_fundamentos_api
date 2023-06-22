import os
os.system('cls'if os.name=='nt'else 'clear')

print('Vamos calcular a area de um retangulo')
lado1 = input('Informe o 1º lado: ')
lado2 = input('Informe o 2º lado: ')
# o metódo isnumeric e isdecimal validam se a string contem apenas digitos numericos
print('Lado1 é um numero inteiro?', lado1.isnumeric())
print('Lado2 é um numero real?', lado2.isdecimal())
area = float(lado1)*float(lado2)
print(type(area))
print('A área do retangulo formada pelos lados {} e {} é igual a {}'.format(lado1, lado2, area))