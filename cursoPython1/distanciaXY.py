import math
def main():
    x1 = int(input('Entre com a cordenada x do primeiro ponto: '))
    y1 = int(input('Entre com a cordenada y do primeiro ponto: '))
    x2 = int(input('Entre com a cordenada x do segundo ponto: '))
    y2 = int(input('Entre com a cordenada y do segundo ponto: '))
    distancia = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
    if distancia < 10:
        print('perto')
    else:
        print('longe')
main()