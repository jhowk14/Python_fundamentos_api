def divisao(x, y):
  try:
    print("Divisao: ", float(x)/float(y))
  except ZeroDivisionError as erro:
    print(erro)
  except:
    print("Ocorreu um erro")