def inverte(lista):
    i = len(lista) - 1
    while i >= 0:
        print(lista[i])
        i -= 1
def main():
    aux = 1
    lista = []
    while aux != 0:
        aux = int(input('Digite um número: '))
        if aux != 0:
            lista.append(aux)
    inverte(lista)
main()