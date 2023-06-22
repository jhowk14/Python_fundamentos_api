
import funcoes
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
      funcoes.soma(x, y)
  if(operador==2):
      funcoes.subtracao(x, y)
  if(operador==3):
      funcoes.multiplicacao(x, y)
  if(operador==4):
      funcoes.divisao(x, y)

  opcao = input("\nAperte 0 para Sair ou Enter para continuar")
  if opcao=="0":
    opcao=int(opcao)
  else:
    opcao=1