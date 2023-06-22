from os import system, name
system('cls') if(name == 'nt') else system('clear')
opcao = ''
listaNome = []
listaCelular = []
while opcao!=' ':
  nome = input("Informe o nick: ")
  celular = input("Informe o id: ")
  listaNome.append(nome)
  listaCelular.append(celular)
  opcao=input('\nAperte espaço para Finalizar o cadastro ou qualquer tecla para continuar ')

for i in range(len(listaNome)):
  print('Nome: ', listaNome[i], ' - Celular:' , listaCelular[i])