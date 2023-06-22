"""
  Cap03 - Atividade 01
  Verificar Número Par e Impar

  Objetivos:
  Nesta atividade você vai usar uma estrutura de decisão (if / else) para verificar se um número é par ou ímpar.

  Comandos utilizados:
  If, operador % (retorna o resto da divisão entre operandos)
"""
from os import system, name
system('cls') if(name =='nt') else system('clear')
numero = int(input('Informe um número: '))
resto = int(numero % 2)
if resto==0:
    resposta='par'
else:
    resposta = 'impar'
print(f'O número {numero} é {resposta}')