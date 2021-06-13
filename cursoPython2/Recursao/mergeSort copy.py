def mergeSort(lista, inicio = 0, fim = None):
    if fim == None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        # chuta pra cima até chegar em tamanho 1 na esquerda, depois na direita
        mergeSort(lista, inicio, meio)
        mergeSort(lista, meio, fim)
        # ordena, desde tamanhos 1 até a lista inteira
        merge(lista, inicio, meio, fim)
def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    rigth = lista[meio:fim]
    topoLeft, topoRigth = 0, 0
    for k in range(inicio, fim):
        if topoLeft >= len(left) or topoRigth >= len(rigth):
            # se pilha da esquerda vazia, resto da lista preenchida com a pilha direita
            if topoLeft >= len(left):
                lista[k] = rigth[topoRigth]
                topoRigth += 1
            # se pilha da DIREITA vazia, resto da lista preenchida com a pilha ESQUERDA
            if topoRigth >= len(rigth):
                lista[k] = left[topoLeft]
                topoLeft += 1
        else:
            # topo esquerdo menor que direito
            if left[topoLeft] < rigth[topoRigth]:
                lista[k]= left[topoLeft] # lista pega topo esquerdo
                topoLeft += 1 # passamos para a proxima carta da pilha esquerda
            else: # topo direito menor que esquerdo
                lista[k] = rigth[topoRigth]
                topoRigth += 1
lista = [10,9,8,7,5,4,3,2,1]
mergeSort(lista)
print(lista)