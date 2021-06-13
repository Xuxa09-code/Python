def conta_letras(frase, contar="vogais"):
    contV = ContC = 0
    assert contar == "vogais" or contar == "consoantes"
    for letra in frase:
        vg = letra.upper()
        if vg == 'A' or vg == 'E' or vg == 'I' or vg == 'O' or vg == 'U':
            contV += 1
        else:
            if 65 <= ord(vg) <= 90:
                ContC += 1
    if contar == 'vogais':
        return contV
    else:
        return ContC