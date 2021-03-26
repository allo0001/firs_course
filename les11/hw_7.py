class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'({self.a} + i{self.b})'

    def __add__(self, other):
        return Complex(self.a+other.a, self.b+other.b)

    def __sub__(self, other):
        return Complex(self.a-other.a, self.b-other.b)

    def __mul__(self, other):
        return Complex(self.a*other.a - self.b*other.b, self.a*other.b + other.a*self.b)


c1 = Complex(6, 5)
c2 = Complex(4, 3)
print(c1)
print(c1+c2)
print(c1-c2)
print(c1*c2)
