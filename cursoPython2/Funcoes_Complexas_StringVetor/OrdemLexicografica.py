def primeiro_lex(lista):
    minimo = lista[0]
    for palavra in lista:
        if palavra < minimo:
            minimo = palavra
    return minimo