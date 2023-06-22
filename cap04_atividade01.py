from os import system, name
system('cls') if (name=='nt') else system('clear')

print('****Tabuada Simples****')
multiplicador = int(input('informe o multiplicador: '))

for i in range(11):
    print(f'{multiplicador} * {i} = {i*multiplicador}')