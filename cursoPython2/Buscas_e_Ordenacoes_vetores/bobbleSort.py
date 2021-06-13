def bubble_sort(lista):
    for i in range(len(lista) - 1, 0, -1):
        trocou = False
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
                trocou = True
        if not(trocou):
            return lista
    return lista
# o = Ordenacoes()
# lista = o.cria(20)
# print(bubble_sort(lista))