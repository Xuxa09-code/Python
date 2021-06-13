def main():
    n = input('Digite um número inteiro: ')
    limite = len(n)
    nInt = int(n)
    soma = 0
    while(limite >= 0):
        soma = soma + (nInt // (10**limite))
        nInt = nInt % (10**limite)
        limite -= 1
    print(soma)
main()