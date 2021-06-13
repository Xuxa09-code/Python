import random
def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0,1000))
    return lista