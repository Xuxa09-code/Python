def main():
    n = input('Digite um número inteiro: ')
    limite = len(n)
    nInt = int(n)
    anterior = nInt // 10**limite
    limite -= 1
    adjacente = False
    while limite >= 0 and not(adjacente) and len(n)>1:
        posicao = nInt // 10**limite
        nInt = nInt % 10**limite
        if posicao == anterior:
            adjacente = True
        anterior = posicao
        limite -= 1
    if adjacente:
        print('sim')
    else:
        print('não')
main()