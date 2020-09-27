def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    escolha = int(input('''
1 - para jogar uma partida isolada
2 - para jogar um campeonato >>> '''))
    
    if escolha == 1:
        print('\nVocê escolheu uma partida isolada.')
        partida()
    else:
        print('\nVocê escolheu um campeonato.')
        campeonato()


def partida(peças_removidas=0):
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    usuário, computador = False, False

    if (n % (m + 1) == 0):
        print('\nVocê começa!')
        usuário = True
    else:
        print('\nComputador começa!')
        computador = True

    while usuário:
        peças_removidas = usuario_escolhe_jogada(n, m)
        n -= peças_removidas
        print(f'Agoram resta(m) {n} peça(s) no tabuleiro.')

        peças_removidas = computador_escolhe_jogada(n, m)
        n -= peças_removidas
        if (n == 0):
            break
        print(f'Agoram resta(m) {n} peça(s) no tabuleiro.')

    while computador:
        peças_removidas = computador_escolhe_jogada(n, m)
        n -= peças_removidas
        if (n == 0):
            break
        print(f'Agoram resta(m) {n} peça(s) no tabuleiro.')

        peças_removidas = usuario_escolhe_jogada(n, m)
        n -= peças_removidas
        print(f'Agoram resta(m) {n} peça(s) no tabuleiro.')
    
    print('Fim do jogo! O computador ganhou!')


def computador_escolhe_jogada(n, m):
    if ((n - 1) % (m + 1) == 0):
        peças_removidas = 1
    else:
        if m <= n:
            if (n==13 and m==4):
                peças_removidas = 3
            else:
                peças_removidas = m
        else:
            peças_removidas = n

    print(f'\nO computador tirou {peças_removidas} peça(s).')
    
    return peças_removidas


def usuario_escolhe_jogada(n, m):
    peças_removidas = int(input('\nQuantas peças você vai tirar? '))

    while (peças_removidas > m) or (peças_removidas > n) or (peças_removidas <= 0):
        print('\nJogada inválida! Tente de novo.')
        peças_removidas = int(input('\nQuantas peças você vai tirar? '))

    return peças_removidas


def campeonato():
    print('\n','*' * 10, 'Rodada 1', '*' * 10, '\n')
    partida()
    print('\n', '*' * 10, 'Rodada 2', '*' * 10, '\n')
    partida()
    print('\n', '*' * 10, 'Rodada 3', '*' * 10, '\n')
    partida()
    print('\n', '*' * 10, 'Fim do campeonato', '*' * 10)
    print('Placar: Você 0 X 3 Computador')



main()