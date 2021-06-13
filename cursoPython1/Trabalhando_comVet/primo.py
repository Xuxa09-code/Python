def main():
    n = int(input('Digite um número inteiro: '))
    i = n - 1
    primo = True
    if n == 0:
        primo = False
    while i > 1 and primo:
        if(n % i == 0):
            primo = False
        i -= 1
    if primo:
        print('primo')
    else:
        print('não primo')
main()