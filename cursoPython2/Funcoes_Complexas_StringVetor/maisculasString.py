def maiusculas(string):
    maiuculas = ''
    for i in range(len(string)):
        if 65 <= ord(string[i]) <= 90:
            maiuculas += string[i]
    return maiuculas
print(maiusculas('PrOgRaMaMoS em python!'))