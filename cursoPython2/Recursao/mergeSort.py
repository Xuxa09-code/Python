def mergeSort(lista, inicio = 0, fim = None):
    if fim == None:
        fim = len(lista)
    if (fim - inicio) > 1:
        meio = (inicio + fim) // 2
        mergeSort(lista, meio, fim)
        mergeSort(lista,inicio, meio)
        print(inicio, fim)
        print(lista)
        merge(lista,inicio, meio, fim)
def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    rigth = lista[meio:fim]
    print(left, '\n\n', rigth)
    i, j = 0, 0
    for k in range(inicio, fim):
        if i >= len(left) or j >= len(rigth):
            if i >= len(left):
                lista[k] = rigth[j]
                j += 1
            if j >= len(rigth):
                lista[k] = left[i]
                i += 1
        else:
            if left[i] > rigth[j]:
                lista[k] = rigth[j]
                j += 1
            else:
                lista[k] = left[i]
                i += 1
lista = [10,9,8,7,6,5,4,3,2,1,0]
mergeSort(lista)
print(lista)