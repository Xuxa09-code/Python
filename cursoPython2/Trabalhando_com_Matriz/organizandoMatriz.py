def imprime_matriz(matriz):
    for linha in matriz:
        for coluna in range(len(linha) - 1):
            print(linha[coluna], end=" ")
        print(linha[len(linha) - 1])