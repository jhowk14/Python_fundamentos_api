import os
os.system('cls'if os.name=='nt'else 'clear')

nomeCompleto = input('Informe seu nome completo: ')

# função len retorno a quantidade de caracteres de uma variável
print('1. Quantidade de caracteres: ', len(nomeCompleto))

# upper = transforma um texto em maiusculo
print('2. Nome em maiusculo:', nomeCompleto.upper())
# lower = transforma um texto em minusculo
print('3. Nome em minusculo:', nomeCompleto.lower())
# capitalize = somente a primeira letra em maiusculo
print('4. Primeira letra em maiusculo:', nomeCompleto.capitalize())

#Primeiro nome
# metodo find sendo usado para localizar o primeiro espaço em branco
espaco = nomeCompleto.find(' ')
# usando a primeira posição de espaco para separar o texto usando a notação [x:x] 
print('5. Somente o primeiro nome:', nomeCompleto[0:espaco])
print('5. Somente o sobrenome:', nomeCompleto[espaco+1:len(nomeCompleto)])

# metodo replace para tirar todos os espacos em branco
print('6. Nome sem espaços:', nomeCompleto.replace(' ', ''))
somenteLetras = nomeCompleto.replace(' ', '')
# metodo isaplha para verificar se tem somente letras na palavra
print('7. Tem somente letras? (temos que tirar os espaços para verificar:', somenteLetras.isalpha())

# metodo isaplha para verificar se tem somente letras ou numeros na palavra
print('8. É alfanumerico? tem letras ou numeros (temos que tirar os espaços para verificar:', somenteLetras.isalnum())

# metodo split para criar uma lista com os nomes usando o espaço em branco como quebra
print('9. Quebrar os texto a cada espaço em branco:', nomeCompleto.split(" "))

# metodo center para centrarlizar o texto em 80 colunas usando o *
print('10. Centralizar o nome entre *')
print(nomeCompleto.center(80,"*"))