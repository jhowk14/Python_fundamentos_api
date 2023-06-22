from os import system, name
system('cls') if(name == 'nt') else system('clear')

numeros = [1,2,3,4,5]
letras = ['a', 'b', 'c', 'd', 'e']
print(numeros)
print(letras)
print('Concatenando listas com o operador +')
concat = numeros+letras
print(concat)

print('Concatenando listas com extend')
numeros.extend(letras)
itens = numeros
print(itens)

print('Desistruturando lista e operador Rest*')
item1, item2, item3, item4, *outros, item8, item9 = itens
print(item1, item2)
print(outros)
print(item8, item9)


print(itens)
print('Iterar Listas - For in')
for i in itens:
    print(i)
    
print('Iterar Listas - For range')
for i in range(len(itens)):
    print(itens[i])