"""
  Cap02 - Atividade 01
  Objetivo receber e somar dois números armazena-los em  variaveis e 
"""
import os
os.system('cls' if os.name=='nt' else 'clear')

print("Seja Bem vindo!")
print("Vamos fazer a soma de dois números inteiros.")
nunero1=input('Informe o 1º numero: ')
numero2=input('Informe o 2º numero: ')
soma = nunero1+numero2
print('A soma entre {} e {} é igual a {}'.format(nunero1, numero2, soma))
#O comando TYPE verifica o tipo de uma variável
print('Os tipos das variaveis que recebem a resposta de um input são do tipo {}' .format(type(nunero1)))
print('É necessário converter')
# Use o int para convertar para números inteiros
soma = int(nunero1)+int(numero2)
print('O tipo da variavel soma agora é {}'.format(type(soma)))
print('Agora sim, a soma entre {} e {} é igual a {}'.format(nunero1, numero2, soma))