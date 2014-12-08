def number_to_list(n):
    n = list(str(n))
    new = []
    number = 0
    for item in n:
        number = int(item)
        new.append(number)
    return new
