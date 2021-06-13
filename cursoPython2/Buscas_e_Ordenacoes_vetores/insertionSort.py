def insertion_sort(lista):
    for i in range(1,len(lista)): # segunda posicao até o final da lista + uma posicao
        aux = lista[i]
        j = i - 1 # o j vai percorrer todo vetor, pos i vai ate uma posicao apos a posicao final
        while j > -1 and lista[j] > aux:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = aux
    return lista