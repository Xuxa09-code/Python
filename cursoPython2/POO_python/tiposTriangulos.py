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