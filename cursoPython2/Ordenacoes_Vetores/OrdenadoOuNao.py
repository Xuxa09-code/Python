def ordenada(lista):
    for i in range(len(lista) - 1):
        minimi_valor = i
        for j in range(i + 1,len(lista)):
            if lista[minimi_valor] > lista[j]:
                return False
    return True