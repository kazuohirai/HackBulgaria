def prime_factorization(n):
    div = 2
    num = n
    divisors = []
    power = 0
    for i in range(0, n):
        if num % div == 0:
            power += 1
            num /= div
        elif num % div != 0 and power != 0:
            divisors.append((div, power))
            div += 1
            power = 0
        else:
            div += 1
    return divisors
