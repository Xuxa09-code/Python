def dimensoes(matriz):
    linha = len(matriz)
    max = 0
    for i in range(0,linha):
        aux = len(matriz[i])
        if aux > max:
            coluna = aux
    print(str(linha)+'X'+str(coluna))