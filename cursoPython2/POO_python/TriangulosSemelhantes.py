class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimetro(self):
        a, b, c = self.a, self.b, self.c
        return a + b + c 
    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c or self.c == self.b:
            return 'isóceles'
        else:
            return 'escaleno'

    def retangulo(self):
        retangulo = False
        if ((self.a ** 2 + self.b ** 2 == self.c ** 2)
        or (self.a ** 2 + self.c ** 2 == self.b ** 2)
        or (self.c ** 2 + self.b ** 2 == self.a ** 2)):
            retangulo = True
        return retangulo

    def soma(self,triangulos):
        return max(triangulos[0]) / max(triangulos[1])

    def confereExclui(self,triangulos):
        if max(triangulos[0]) % max(triangulos[1]) == 0:
            resultado = 1
        else:
            resultado = 0
        del (triangulos[0][triangulos[0].index(max(triangulos[0]))],
             triangulos[1][triangulos[1].index(max(triangulos[1]))])
        return resultado

    def semelhantes(self,triangulo):
        cont = i = 0
        res = []
        semelhante1 = [[triangulo.a, triangulo.b, triangulo.c], [self.a, self.b, self.c]]
        semelhante1Aux = [[],[]]
        if semelhante1[0] != semelhante1[1]:
            semelhante1Aux[0] = max(semelhante1[0],semelhante1[1])
            semelhante1Aux[1] = min(semelhante1[0],semelhante1[1])
        else:
            semelhante1Aux[0], semelhante1Aux[1] = semelhante1[0],semelhante1[1]
        while i < 3:
            res += [self.soma(semelhante1Aux)]
            cont += self.confereExclui(semelhante1Aux)
            i += 1
        if cont == 3 and res[0] == res[1] == res[2]:
            return True
        else:
            return False