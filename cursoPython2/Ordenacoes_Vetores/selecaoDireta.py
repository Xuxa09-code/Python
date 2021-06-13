import random
a = []
for i in range(10000):
    a.append(random.randint(0,1000))
print(a)
for i in range(len(a) - 1):
    posicao_minimo = i
    for j in range(i +1, len(a)):
        if a[posicao_minimo] > a[j]:
            posicao_minimo = j
    a[i],a[posicao_minimo] = a[posicao_minimo],a[i]
    print('\n\n', a)