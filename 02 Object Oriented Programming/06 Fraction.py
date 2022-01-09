
class Fraction:

    def __init__(self, num=0, den=1):
        self.num = num
        self.den = den
        self.reduce()


    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value

    @property
    def den(self):
        return self._den

    @den.setter
    def den(self, value):
        # on your own, prevent a zero denominator
        self._den = value  

    def to_decimal(self):
        return self.num / self.den

    def reduce(self):
        gcd = 1
        minumum = min(abs(self.num), abs(self.den))

        for i in range(2, int(minumum) + 1):
            if self.num % i == 0 and self.den % i == 0:
                gcd = i

        self.num = int(self.num / gcd)
        self.den = int(self.den / gcd)

        if self.num == 0:
            self.den = 1

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        result = Fraction(num, den)
        result.reduce()
        return result

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __str__(self):
        return f"{self.num} / {self.den}  ({self.to_decimal()})"

f1 = Fraction()
print(f1)
f4 = Fraction(2, 3)

f2 = Fraction(5, 10)
print(f2)

f3 = f2 + f4
print(f3)

