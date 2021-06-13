def soma(m1,m2):
    soma = []
    lista = []
    for i in range(len(m1)):
        lista = []
        for j in range(len(m1[i])):
            lista.append(m1[i][j] + m2[i][j])
        soma.append(lista)
    return soma
def soma_matrizes(m1, m2):
    iguais = False
    if len(m1) == len(m2):
        iguais = False
        for coluna in range(len(m1)):
            if len(m1[coluna]) == len(m2[coluna]):
                iguais = True
    if not iguais:
        return False
    else:
        return soma(m1,m2)