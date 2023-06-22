# def = função
def soma(x, y):
  try:
    print("Soma: ", float(x)+float(y))
  except:
    print("Ocorreu um erro")

def subtracao(x, y):
  try:
    print("Subtracao: ", float(x)-float(y))
  except:
    print("Ocorreu um erro")

def multiplicacao(x, y):
  try:
    print("Multiplicacao: ", float(x)*float(y))
  except:
    print("Ocorreu um erro")

def divisao(x, y):
  try:
    print("Divisao: ", float(x)/float(y))
  except ZeroDivisionError as erro:
    print(erro)
  except:
    print("Ocorreu um erro")