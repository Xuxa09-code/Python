class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimetro(self):
        a, b, c = self.a, self.b, self.c
        return a + b + c 