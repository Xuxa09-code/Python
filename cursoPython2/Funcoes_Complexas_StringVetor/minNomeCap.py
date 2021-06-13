def menor_nome(nomes):
    min = nomes[0].strip().capitalize()
    for i in range(len(nomes)):
        nomes[i] = nomes[i].strip().capitalize()
        if len(nomes[i]) < len(min):
            min = nomes[i]
    return min
print(menor_nome(['zé', ' lu', 'fê']))