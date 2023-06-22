from classe import *
data="30/04/2022" 
nome="Joaquim da Silva" 
endereco="Rua dos Pombos, 000"
carrinho=CarrinhoCompras( data, nome, endereco)
carrinho.addProduto('Notebook Dell i7', 5800)
carrinho.addProduto('SmartPhone', 2800)
carrinho.addProduto('XBox', 3400)
print(f'Carrinho: {carrinho.data}')
print('Cliente',carrinho.cliente.nome)
print('Endereco',carrinho.cliente.endereco)
print('-----')
total=carrinho.calcularTotal()
print(f'Total R${total}')
print('---')


