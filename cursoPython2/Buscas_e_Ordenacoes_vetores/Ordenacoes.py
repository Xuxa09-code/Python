import random
class Ordenacoes:
    def cria (self, tamanho, minimo = 0, maximo = 1000):
        '''Gera uma lista randomica com tamanho definido pelo usuario'''
        # comando abaixo gera uma lista com elementos randomicos
        return [random.randint(minimo, maximo) for x in range(tamanho)]
    def selecaoDireta(self, a):
        for i in range(len(a) - 1):
            posicao_minimo = i
            for j in range(i +1, len(a)):
                if a[posicao_minimo] > a[j]:
                    posicao_minimo = j
            a[i],a[posicao_minimo] = a[posicao_minimo],a[i]
    def selectionSort(self, lista):
        for i in range(len(lista) - 1):
            indice_minimo = i
            for j in range(i + 1, len(lista)):
                if lista[j] < lista[indice_minimo]:
                    indice_minimo = j
            if indice_minimo != i:
                lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    def bobblesort_rapido(self, lista):
        i = len(lista) - 1
        trocou = True
        while i > 0 and trocou:
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            i -= 1
    def bobblesort(self, lista):
        i = len(lista) - 1
        while i > 0:
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            i -= 1
    def insercaoDireta(self, lista):
        for i in range(1,len(lista)): # segunda posicao até o final da lista + uma posicao
            aux = lista[i] # guarda o valor na posicao i dando a oportunidade de modica-lo
            j = i - 1
            while j > -1 and lista[j] > aux: # passa para a direita todos valores maiores que o valor aux
                lista[j+1] = lista[j]
                j -= 1
            lista[j+1] = aux # lista[j+1] pega o valor q foi usado de parametro no laço anterior
class Buscas():
    def sequencial(self, lista, elem):
        for elemento in lista:
            if elemento == elem:
                return lista.index(elem)
        return -1
    def binario(self, lista, elem):
        inicio = 0
        fim = len(lista) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if elem == lista[meio]:
                return meio
            else:
                if elem > lista[meio]:
                    inicio = meio + 1
                else:
                    fim = meio - 1
        return -1
# o = Ordenacoes()
# lista = o.cria(100)
# o.bobblesort_rapido(lista)
# print(lista)
# b = Buscas()
# print(b.binario(lista, 10), end='\n\n\n')
# print(b.sequencial(lista, 10))