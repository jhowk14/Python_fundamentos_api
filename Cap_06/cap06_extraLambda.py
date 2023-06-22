
from os import system, name
soma = lambda x, y: x+y
subtracao = lambda x, y: x-y
multiplicacao = lambda x, y: x*y
divisao = lambda x, y: x/y

opCalculo=(soma, subtracao, multiplicacao, divisao)
opTexto=('Soma', 'Subtração', 'Multiplicação', 'Divisão')
while (True):
    system('cls') if(name == 'nt') else system('clear')
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")

    op = int(input("Opção: "))-1
    print(f'{opTexto[op]}: {opCalculo[op](x, y)}')
    opcao = input('\nAperte "S" para Sair ou Enter para continuar... ')
    if opcao.lower()=="s":
        break