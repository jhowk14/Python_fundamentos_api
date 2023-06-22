from os import system, name
system('cls') if(name == 'nt') else system('clear')

pessoa={
    'nome':'José',
    'idade':40,
    'cidade':'Pindorama',
}
print('Criar dicionário de dados')
print(pessoa)
print('Modificar valores em dicionários de dados')
pessoa['idade'] = 35
pessoa.update({'nome':'Maria', 'Endereco': 'Rua dos Pombos, n.000' , 'cidade': 'Catanduva'})
print(pessoa)
print('Exibir informações baseado em chave/valor')
print(pessoa['nome'])
#print(pessoa['estadoCivil'])
print(pessoa.get('estadoCivil', 'Indefinido'))
print('Remover chave/valor em dicionários de dados')
del pessoa['idade']
print('Pessoa agora possue apenas ', len(pessoa), 'chaves')
print(pessoa)
print('Iterando dicionários de dados')

print('Apenas chaves')
for i in pessoa.keys():
    print(i)
print('Apenas Valores')
for i in pessoa.values():
    print(i)
print('Chaves e Valores')
for k, v in pessoa.items():
    print(k,':', v)


