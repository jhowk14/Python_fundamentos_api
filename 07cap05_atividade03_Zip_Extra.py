from os import system, name
system('cls') if(name == 'nt') else system('clear')
opcao = ''
listaNome = []
listaCelular = []
listacidades= []
while opcao!='x':
  nome = input("Informe o nome: ")
  celular = input("Informe o celular: ")
  cidade = input('informe a cidade')
  listaNome.append(nome)
  listaCelular.append(celular)
  listacidades.append(cidade)
  opcao=input('\nAperte X para Finalizar o cadastro ou qualquer tecla para continuar ')

#Utilização do metodo Zip para concatenar as listas
dados = zip(listaNome, listaCelular)
registros=list(dados)
for i in registros:
  print(('Nome: ', i[0], ' - Celular:' , i[1], ' -cidade:', i[2]))          