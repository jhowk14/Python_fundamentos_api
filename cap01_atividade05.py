"""
  Cap01-Atividade 05
  Objetivo é introduzir os comandos input e format

"""
#Importando a biblioteca 'os' e passando o comando de limpar tela para o console
import os
os.system('cls' if os.name=='nt' else 'clear')

#Mensagem de boas vindas e contatenação com o operador + 
print('Seja bem-vindos a aula de '+'Python')

#Entrada de dados com input e .format para concatenar string
print('Olá {}'.format(input('Qual o seu nome?')))