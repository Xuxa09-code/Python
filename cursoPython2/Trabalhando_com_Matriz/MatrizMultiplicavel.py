def sao_multiplicaveis(m1, m2):
    elementoMat1 = len(m1[0])
    for elemento in m1:
        if len(elemento) != elementoMat1:
            return False
    elementoMat2 = len(m2[0])
    for elemento in m2:
        if len(elemento) != elementoMat2:
            return False
    if elementoMat1 == len(m2):
        return True
    else:
        return False
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(sao_multiplicaveis(m1, m2))

m1 = [[1,1], [2,1], [3,1]]
m2 = [[1, 2, 3],[1, 2, 3]]
print(sao_multiplicaveis(m1, m2))