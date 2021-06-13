def nFatorial(n):
    if n == 0:
        return 1
    else:
        return n*nFatorial(n-1)
def main():
    n = int(input('Entre com um número para n: '))
    k = int(input('Entre com um número para k: '))
    if n > k:
        resultado = nFatorial(n) / ( nFatorial(k) * nFatorial(n-k))
    else:
        resultado = 0
    print(resultado)
main()