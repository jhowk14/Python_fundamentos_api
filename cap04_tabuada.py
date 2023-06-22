from os import system, name
system('cls') if (name=='nt') else system('clear')

print('\n***** multi tabuada *****')
for i in range(1, 11):
    print(f'{i:>4}, {i*2:>4}, {i*3:>4}, {i*4:>4}, {i*5:>4}, {i*6:>4}, {i*7:>4}, {i*8:>4}, {i*9:>4}, {i*10:>4},')
print('\n*** multi tabuada 2 ***')

for i in range(1, 11):
    linha = f'{i: >4}'
    for il in (range(2, 11)):
        linha+=f'{il*i: >4} '
    print(linha)