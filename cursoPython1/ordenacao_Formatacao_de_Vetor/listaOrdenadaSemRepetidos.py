def remove_repetidos(lista):
    lista2 = sorted(lista)
    print(lista2)
    i = 0
    while i < len(lista2):
        j = 0
        while j < len(lista2):
            if lista2[i] == lista2[j] and i != j:
                del lista2[j]
            j += 1
        i += 1
    return lista2