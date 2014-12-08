def prepare_meal(number):
    n = 1
    meal = ""
    if number == 3:
        return "spam"
    if number % 3 == 0:
        while (3 ** n) <= number:
            if number % (3 ** n) == 0:
                meal += "spam "
            n += 1
    meal = meal[:-1]
    if number % 5 == 0 and number % 3 == 0:
        meal += " and eggs"
    if number % 5 == 0 and number % 3 != 0:
        meal += "eggs"
    return meal
