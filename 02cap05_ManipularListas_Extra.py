from os import system, name
system('cls') if(name == 'nt') else system('clear')

capitais=["São Paulo", "Porto Alegre", "Curitiba", "Rio de Janeiro"]
#capitais = input("Digite nome de capitais do Brasil")
#capitais = capitais.split(', ')
print(capitais)
print('Inser item no final com append')
capitais.append('Florianópolis')
print(capitais)
print('Remover item no final com remove')
capitais.remove('Rio de Janeiro')
print('Inser item na posição específica(2) com insert')
capitais.insert(2, 'Florianópolis')
print(capitais)
print('Inser item na posição específica(4) com pop')
capitais.pop(4)
print(capitais)
print('Ordenação com sort')
capitais.sort()
print(capitais)
