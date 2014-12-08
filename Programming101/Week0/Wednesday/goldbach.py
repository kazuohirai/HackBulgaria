def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    if n % 2 != 0:
        return False
    if n <= 0:
        return False

    subtract = 1
    half = n / 2
    l = []
    while subtract <= half:
        number = n - subtract
        if is_prime(subtract) and is_prime(number):
            l.append((subtract, number))
        subtract += 1
    return l
