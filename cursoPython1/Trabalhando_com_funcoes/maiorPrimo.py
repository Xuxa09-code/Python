def maior_primo(numero):
    primo = True
    while primo and numero >= 0:
        n = numero - 1
        while n > 1 and primo:
            if numero % n == 0:
                primo = False
            n -= 1
        if not primo:
            primo = True
        else:
            return numero
        numero -= 1
# def main():
#     numero = int(input('Entre com o número desejado: '))
#     print(maior_primo(numero))
# main()