import math

def main():
    a = int(input('Entre com o valor de A: '))
    b = int(input('Entre com o valor de B: '))
    c = int(input('Entre com o valor de C: '))
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        if x1<x2:
            print('as raízes da equação são',x1,'e',x2)
        else:
            print('as raízes da equação são',x2,'e',x1)
    else:
        if delta == 0:
            x = (-b + math.sqrt(delta))/(2*a)
            print('a raiz desta equação é',x)
        else:
            print('esta equação não possui raízes reais')
main()