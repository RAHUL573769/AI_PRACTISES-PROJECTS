
class Fraction1:

    def __init__(self, x, y):
        self.num = x
        self.den = y

    def __str__(self):
        result2 = "{}/{}".format(self.num, self.den)
        return result2


fraction = Fraction1(12, 45)
print(fraction)
