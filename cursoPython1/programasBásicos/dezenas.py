def main():
    valor = int(input('Digite um número inteiro: '))
    resCentena = valor % 100
    dezena = resCentena // 10
    print('O dígito das dezenas é',dezena)
main()