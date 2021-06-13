def maximo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
# def main():
#     a = int(input('Entre com o valor de a: '))
#     b = int(input('Entre com o valor de b: '))
#     c = int(input('Entre com o valor de c: '))
#     print(maximo(a, b, c))
# main()