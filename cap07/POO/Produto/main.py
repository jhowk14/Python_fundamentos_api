from classe import Produto
notebook = Produto('Notebook Dell i7', 5800.90)
print(notebook.descricao, notebook.preco)
notebook.verProduto()
input('Pressione qualquer tecla para ver a oferta: ')
notebook.descricao="Notebook Acer i5"
notebook.preco=4800
print(notebook.descricao, notebook.preco)
notebook.verProduto()

