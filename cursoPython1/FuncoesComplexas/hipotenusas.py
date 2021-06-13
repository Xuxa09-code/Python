def é_hipotenusa(n):
    c1 = 1
    hipotenusa = False
    while (not hipotenusa) and c1 < n:
        c2 = n -1
        while c2 > 1:
            if c1**2 + c2**2 == n**2:
                # print(c1,c2)
                hipotenusa = True
            c2 -= 1
        c1 += 1
    return hipotenusa
def soma_hipotenusas(n):
    # n = 0
    # while n < 1:
    #     n = int(input('Entre com um numero maior que 1: '))
    #     if n < 1:
    #         print('Numero invalido!!!')
    i = 1
    soma = 0
    while i <= n:        
        if é_hipotenusa(i):
            soma += i
        i += 1
    return soma

# def main():
#     n = 0
#     while n < 1:
#         n = int(input('Entre com um numero maior que 1: '))
#         if n < 1:
#             print('Numero invalido!!!')
#     soma_hipotenusas(n)
# main()