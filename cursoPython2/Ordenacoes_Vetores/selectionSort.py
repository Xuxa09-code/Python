import random
def ordena(lista):
    for i in range(len(lista) - 1):
        indice_minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        if indice_minimo != i:
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista