def n_primos (n):
    cont = 0
    while n > 1:
        i = n - 1
        primo = True
        while i > 1 and primo:
            if(n % i == 0):
                primo = False
            i -= 1
        if primo:
            cont += 1
        n -= 1
    return cont
# def main():
#     n = int(input('Entre com um numero: '))
#     print(n_primos(n))
# main()