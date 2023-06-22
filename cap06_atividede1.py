from os import system, name

def soma(x, y):
    print("soma: ", x+y)

def subtração(x, y):
    print("subtração: ", x-y)

def multiplicação(x, y):
    print("multiplicação; ", x*y)

def divisão(x, y):
    print("divisão: ", x/y)

while (True):
    system('cls') if (name=='nt') else system('clear')
    x = float(input("primeiro numero: "))
    y = float(input("segundo numero: "))
    print("1. soma")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    operador = int(input("opção: "))
    if(operador==1):
        soma(x, y)
    if(operador==2):
        subtração(x, y)
    if(operador==3):
        multiplicação(x, y)
    if(operador==4):
        divisão(x, y)
    opcao = input('\nAperte "s" para sair ou enter para continuar... :')
    if opcao.lower()=='s':
        break