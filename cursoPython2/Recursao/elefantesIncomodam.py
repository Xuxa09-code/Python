def incomodam(n, incomodamString = ''):
    if n >= 1:
        incomodamString += "incomodam "
        return incomodam(n - 1, incomodamString)
    return incomodamString
def elefantes(n, limite = 1, stringMusica = ''):
    if limite <= n:
        if limite == 1:
            stringMusica += 'Um elefante incomoda muita gente'
            return elefantes(n, limite + 1, stringMusica)
        else:
            stringMusica += '\n' + str(limite) + ' elefantes ' + incomodam(limite) + 'muito mais'
            if limite != n:
                stringMusica += '\n' + str(limite) + ' elefantes incomodam muita gente'
            return elefantes(n, limite + 1, stringMusica)
    else:
        return stringMusica
print(elefantes(4))