from classe import AssinaturaTv
tv = AssinaturaTv()
print(tv)
print('Canais disponíveis')
print(tv.canaisDisponiveis)
print('---')
print('Canal Ativo')
print(tv.canalAtivo)
print('---')
tv.canalAtivo = 15
print(tv.canalAtivo)
print('---')
tv.canalAtivo = 25
print('Canal Ativo')
print(tv.canalAtivo)
print('---')

