def busca(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    while fim >= inicio:
        meio = (inicio + fim) // 2
        print(meio)
        if lista[meio] == elemento:
            return meio
        else:
            if lista[meio] > elemento:
                fim = meio - 1
            else:
                inicio = meio + 1
    return False