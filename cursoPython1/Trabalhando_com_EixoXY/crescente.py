def main():
    n1 = int(input('Entre com o primeiro numero: '))
    n2 = int(input('Entre com o segundo numero: '))
    n3 = int(input('Entre com o terceiro numero: '))

    if (n1<=n2) and (n1<=n3):
        print('crescente')
    else:
        print('não está em ordem crescente')
main()