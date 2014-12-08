def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


class Fractions():

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return "{}/{}".format(self.num, self.denom)

    def display(self):
        div = 2
        m = max(self.num, self.denom)
        while div <= m and self.denom != 1:
            if self.num % div == 0 and self.denom % div == 0:
                self.num /= div
                self.denom /= div
            elif self.num % div != 0 or self.denom % div != 0:
                div += 1

        if self.denom == 1:
            return self.num
        else:
            return self

    def __add__(self, other):
        x = Fractions(0, 0)
        if self.denom == other.denom:
            x.num = self.num + other.num
            x.denom = self.denom
        else:
            LCM = (self.denom * other.denom) / (gcd(self.denom, other.denom))
            if LCM == self.denom:
                x.num = self.num + ((LCM/other.denom) * other.num)
            if LCM == other.denom:
                x.num = other.num + ((LCM/self.denom) * self.num)
            x.denom = LCM
        return x.display()

    def __sub__(self, other):
        x = Fractions(0, 0)
        if self.denom == other.denom:
            x.num = self.num - other.num
            x.denom = self.denom
        else:
            LCM = (self.denom * other.denom) / (gcd(self.denom, other.denom))
            if LCM == self.denom:
                x.num = self.num - ((LCM/other.denom) * other.num)
            if LCM == other.denom:
                x.num = other.num - ((LCM/self.denom) * self.num)
            x.denom = LCM
        return x.display()

    def __mul__(self, other):
        x = Fractions(0, 0)
        x.num = self.num * other. num
        x.denom = self.denom * other.denom
        return x.display()

    def __div__(self, other):
        x = Fractions(0, 0)
        x.num = self.num * other. denom
        x.denom = self.denom * other.num
        return x.display()

    def __eq__(self, other):
        LCM = self.denom * other.denom / gcd(self.denom, other.denom)
        self.num = self.num * other.denom
        other.num = self.denom * other.num
        self.denom = LCM
        other.denom = LCM
        if self.num == other.num and self.denom == other.denom:
            return True
        return False

    def __big__(self, other):
        LCM = self.denom * other.denom / gcd(self.denom, other.denom)
        self.num = self.num * other.denom
        other.num = self.denom * other.num
        self.denom = LCM
        other.denom = LCM
        if self.num > other.num:
            return True
        return False
