class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def getData(self):
        print(f"{self.real}+{self.imag}j")


c1 = ComplexNumber(2, 3)
c1.getData()
c2 = ComplexNumber(5)
c2.attr = 10

print((c2.real, c2.imag, c2.attr))
