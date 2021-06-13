def main():
    n = int(input('Digite o valor de n: '))
    fatorial = n
    i = 1
    if(n == 0):
        fatorial = 1
    else:
        while i < n:
            fatorial = fatorial*i
            i+=1
    print(fatorial)
main()