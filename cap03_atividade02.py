"""
  Cap03 - Atividade 02
  Conversor de Medidas

  Objetivos:
  Nesta atividade você vai converter um número em centimetros para Polegada, Pé ou Jarda. 
  Será necessário usar o comando if / elif / else.

  Comandos utilizados:
  If / elif / else, formatação de números com posição de substituição {:.4f}
"""
from os import system, name
system('cls') if (name=='nt') else system('clear')

medidaCm = float(input('Informe a medida em centímetros: '))
print('\nEcolha a unidade que deseja converter')
print('1 - Polegada\n2 - Pé\n3 - Jarda')
menu = input('Opção: ')
if menu=='1':
    unidade='Polegada'
    resConversao=medidaCm/2.54
elif menu=='2':
    unidade='Pé'
    resConversao=medidaCm/30.48
elif menu=='3':
    unidade='Jarda'
    resConversao=medidaCm/91.44
else:
    print('Você não escolheu uma opção válida')

print(f'{medidaCm} centímetros correspodendem a {resConversao:.4f} em {unidade}(s)')

