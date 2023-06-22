from sys import getsizeof
from os import system, name
system('cls') if(name == 'nt') else system('clear')


#Iteração com List Comprehension
numeros=[]
for x in range(6):
  numeros.append(x*10)
print(numeros)

numeros = [x*10 for x in range(1, 11)]
print(numeros)
print(getsizeof(numeros))

print('-----------------------')

numeros = (x*10 for x in range(1, 11))
print(list(numeros))
print(getsizeof(numeros))

# List Comprehension em texto e com condicionais
nomes=("Carlos Alberto", "Gustavo", "Jonathan", "José Renato", "Marcelo", "Vinicius")
pesquisaNomes=[nome for nome in nomes if 'J' in nome]
print(pesquisaNomes)