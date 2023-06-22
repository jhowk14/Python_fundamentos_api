from array import array
from os import system, name
system('cls') if(name == 'nt') else system('clear')
listaNumeros = [1,2,3,4,5]
listaLetras = ['a', 'b', 'c', 'd', 'e']
print('Exibição de listas')
print(listaNumeros)
print(listaLetras)
print('Converter para Array') #https://docs.python.org/pt-br/3.7/library/array.html
arrayNumeros = array('i', listaNumeros)
arrayLetras = array('u', listaLetras)
print(arrayNumeros)
print(arrayLetras)
