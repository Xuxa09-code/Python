import math
def deltaF(a,b,c):
    return b**2 - 4*a*c
def baskara(a,b,c,delta):
    return (-b + math.sqrt(delta))/(2*a)
def baskaraN(a,b,c,delta):
    return (-b - math.sqrt(delta))/(2*a)
def main():
    a = int(input('Entre com o valor de A: '))
    b = int(input('Entre com o valor de B: '))
    c = int(input('Entre com o valor de C: '))
    delta = deltaF(a,b,c)
    if delta > 0:
        x1 = baskara(a,b,c,delta)
        x2 = baskaraN(a,b,c,delta)
        if x1<x2:
            print('as raízes da equação são {:.2f} e {:.2f}'.format(x1,x2))
        else:
            print('as raízes da equação são {:.2f} e {:.2f}'.format(x2,x1))
    else:
        if delta == 0:
            x = baskara(a,b,c,delta)
            print('a raiz desta equação é {:.2f}'.format(x))
        else:
            print('esta equação não possui raízes reais')
main()