def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    escolha = int(input('''
1 - para jogar uma partida isolada
2 - para jogar um campeonato '''))
    
    if escolha == 1:
        print('\nVoce escolheu uma partida isolada!')
        partida(1)
    else:
        print('\nVocê escolheu um campeonato!')
        campeonato()


def partida(rodada):
    print()
    print('*' * 4, f' Rodada {rodada} ', '*' * 4)
    print()

    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if (n % (m + 1) == 0):
        print('\nVoce começa!')
    else:
        print('\nComputador começa!')


def campeonato():
    print('Estamos dentro do campeonato')
    partida(1)
    partida(2)
    partida(3)


main()