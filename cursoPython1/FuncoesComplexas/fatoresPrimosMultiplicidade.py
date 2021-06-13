def main():
    n = 0
    while n <= 1:
        n = int(input('Entre com um numero: '))
        if n <= 1:
            print('Numero errado!!!')
    print(n,end=' = ')
    while n > 1:
        fator = 2
        if n % fator == 0:
            n = n/fator
            print(fator, end= ' ')
        else:
            fator += 1
            while n % fator != 0: 
                nPrimo = True
                while nPrimo:
                    fator += 1
                    cont = 0
                    i = fator - 1
                    while i > 1:
                        if(n % i == 0):
                            cont += 1
                        i -= 1
                    if cont < 1:
                        nPrimo = False
            print(fator, end=' ')
            n = n/fator
        if n > 1:
            print('*',end=' ')
        fator +=1            
main()