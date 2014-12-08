from decimal import Decimal
from fractions import Fraction


def simplify_fract(num, denom):
    div = 2
    m = max(num, denom)
    while div <= m and denom != 1:
        if num % div == 0 and denom % div == 0:
            num /= div
            denom /= div
        elif num % div != 0 or denom % div != 0:
            div += 1

    if denom == 1:
        return num
    else:
        return "%d/%d" % (num, denom)


def sort_fractions(fract):
    fracts2 = {}
    fracts = []
    result = 0
    for item in fract:
        a = float(item[0])
        b = float(item[1])
        result = round(float(a / b), 2)
        fracts.append(result)
    for item in fracts:
        item = Fraction(Decimal(item))
    index = 0
    for item in fracts:
        fracts2[item] = fract[index]
        index += 1
    fracts = sorted(fracts)
    fract = []
    for item in fracts:
        fract.append(fracts2[item])
    return fract
