def busca(lista, elemento):
    for elem in range(len(lista)):
        if lista[elem] == elemento:
            return elem
    return False