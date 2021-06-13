def busBinRecursiva(lista, elem, comeco = 0, fim = None):
    if fim == None:
        fim = len(lista) - 1
    meio = (fim + comeco) // 2
    if fim < comeco:
        return -1
    if lista[meio] == elem:
        return meio
    else:
        if lista[meio] < elem:
            return busBinRecursiva(lista, elem, comeco = meio + 1)
        else:
            return busBinRecursiva(lista, elem, comeco = 0, fim = meio - 1)
print(busBinRecursiva([1,2,3,4,5,6,7,8,9,10],11))