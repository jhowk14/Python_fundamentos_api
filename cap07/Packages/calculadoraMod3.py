
from f.soma  import soma
from f.subtracao  import subtracao
from f.multiplicacao  import multiplicacao
from f.divisao  import divisao
opcao=1
while opcao:
  x = float(input("Primeiro numero: "))
  y = float(input("Segundo numero: "))

  print("1. Somar")
  print("2. Subtrair")
  print("3. Multiplicação")
  print("4. Divisão ")

  operador = int(input("Opção: "))
  if(operador==1):
    soma(x, y)
  if(operador==2):
    subtracao(x, y)
  if(operador==3):
    multiplicacao(x, y)
  if(operador==4):
    divisao(x, y)

  opcao = input("\nAperte 0 para Sair ou Enter para continuar")
  if opcao=="0":
    opcao=int(opcao)
  else:
    opcao=1