def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
def main():
    n = int(input('Entre com o valor desejado '))
    while n > 0:
        print('O fatorial de',n,'=',fatorial(n))
        n = int(input('Entre com o valor desejado '))
main()