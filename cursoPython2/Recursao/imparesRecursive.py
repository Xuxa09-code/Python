def encontra_impares(lista, res = []):
    if len(lista) > 0:
        if lista[0] % 2 != 0:
            res.append(lista[0])
        return encontra_impares(lista[1:])
    else:
        return res