def imprime(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j],end=' ')
        print()
def constroi(linha, coluna):
    matriz = []
    for i in range(linha):
        lista = []
        for j in range(coluna):
            lista.append(0)
        matriz.append(lista)
    return matriz
def multiplicaMatriz(matrizA,matrizB):
    assert len(matrizA[0]) == len(matrizB)
    tamanhoK = range(len(matrizA[0]))
    imprime(matrizA)
    print('*'.center(max(len(matrizA[0]),len(matrizB[0]))))
    imprime(matrizB)
    matrizC = constroi(len(matrizA),len(matrizB[0]))
    # print(matrizC)
    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            matrizC[i][j] = 0
            for k in tamanhoK:
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
    print('='.center(len(matrizC[1])+1))
    imprime(matrizC)
    return matrizC
multiplicaMatriz([[5,1],[3,2]],[[0,5,1,6],[2,-1,4,-3]])