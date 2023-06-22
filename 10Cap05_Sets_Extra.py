from os import system, name
system('cls') if(name == 'nt') else system('clear')

lista1=[10, 20, 30, 40, 50]
lista2=[30, 40, 50, 60, 70, 80]

setExemplo={5, 30, 7, 8, 10, 30, 7}
print(setExemplo)
set1=set(lista1)
set2=set(lista2)

print(set1 | set2) #Union (Remove valores repetidos)
print(set1 - set2) #Diference (Retorna apenas os diferentes)
print(set1 ^ set2) # Symmetric Diference(Remove os duplicados)
print(set1 & set2) # And (Retorna apenas os duplicados)
#Sets perdem o index
print('Convertendo novamente para listas')
listaUnion = list(set1 | set2)
print(listaUnion)
listaDiference = list(set1 - set2)
print(listaDiference)
listaSymmetric = list(set1 ^ set2)
print(listaSymmetric)
listaAnd = list(set1 & set2)
print(listaAnd)