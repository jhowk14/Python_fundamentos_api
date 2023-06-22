from os import system, name
system('cls') if(name == 'nt') else system('clear')

capitais=("São Paulo", "Porto Alegre", "Curitiba", "Rio de Janeiro")
print('Leitura do inicio para o final')
print(capitais[0])
print(capitais[1])
print(capitais[2])
print(capitais[3])

print('Leitura do final para o inicio com índices negativos')
print(capitais[-1])
print(capitais[-2])
print(capitais[-3])
print(capitais[0]) # -0 não existe


