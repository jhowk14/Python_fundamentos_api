from os import system, name
import random

opcao = ' '
while opcao.upper()==' ':
    system('cls') if(name == 'nt') else system('clear')

    computador = random.randint(0,2)
    jogador = int(input('''Escolha uma opcao para se jogar: 
    [0] Pedra
    [1] Papel
    [2] Tesoura
    Digite sua escolha: '''))

    pecas = ("Pedra", "Papel", "Tesoura")

    if (jogador > 3):
        resultado = 'Você não escolheu um item correto!!!'
    else:
        print('Você escolheu {}' . format(pecas[jogador]))
        print('O computador escolheu: {}' . format(pecas[computador]))
        tabela = ((0, 1, -1),(-1, 0, 1),(1, -1, 0))
        jogada = tabela[computador][jogador]
        match jogada:       #Funciona apenas a partir da versão 3.7
            case 0:
                resultado = "Deu empate vocês escolheram a mesma peça"
            case 1:
                resultado = "Você ganhou!"
            case -1:
                resultado = "O computador ganhou"

    print(resultado)
    opcao=input('Jogar novamente? Aperte espaço e enter para jogar novamente. ')