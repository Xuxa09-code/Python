def computador_escolhe_jogada(n,m):
    if n < m+1:
        pecas = n
    else:
        if n % (m+1) == 0:
            pecas = m
        else:
            pecas = n % (m+1)
    print()
    if pecas == 1:
        print('O computador tirou uma peça')
    else:
        print('O computador tirou',pecas,'peças')
    return pecas
def usuario_escolhe_jogada(n,m):
    pecas = m+1
    while pecas > m or pecas <= 0:
        print()
        pecas =  int(input('Quantas peças você vai tirar? '))
        if 0 < pecas <= m:
            print()
            if pecas != 1:
                print('Você tirou', pecas, 'peças.')
            else:
                print('Você tirou uma peça.')
        else:
            print('Oops! Jogada inválida! Tente de novo.')
    return pecas
def partidaf():
    print()
    m = n = -10
    while m <= 0 or n <= 0:
        n = int(input('Quantas peças? '))
        m = int(input('Limite de peças por jogada? '))
        if m <= 0 or n <= 0:
            print('Não podemos jogar assim :(')
    print()
    if n % (m+1) == 0:
        l = False
        print('Voce começa!')
    else:
        l = True
        print('Computador começa!')
    while n > 0: 
        if l:
            pecas = computador_escolhe_jogada(n,m)
            n -= pecas
            l = False
        else:
            pecas = usuario_escolhe_jogada(n,m)
            n -= pecas
            l = True
        if n > 0:
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            else:
                print('Agora restam', n,'peças no tabuleiro.')
    print()
    if not l:
        print('Fim do jogo! O computador ganhou!')
        return 1
    else:
        print('Fim do jogo! O usuário ganhou!')
        return -1
def campeonato():
    partida = 1
    pontuacaoC = pontuacaoU = 0
    while partida <= 3:
        print()
        print('**** Rodada',partida,'****')
        if partidaf() > 0:
            pontuacaoC += 1
        else:
            pontuacaoU +=1
        partida += 1
    print('**** Final do campeonato! ****')
    print('Placar: Você', pontuacaoU,'X', pontuacaoC ,'Computador')
    
def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('1 - para jogar uma partida isolada')
    op = int(input('2 - para jogar um campeonato '))
    print()
    if op == 1:
        print('Voce escolheu uma partida isolada!')
        partidaf()
    else:
        print('Voce escolheu um campeonato!')
        campeonato()
main()