def groupby(func, seq):
    dictionary = {}
    for item in seq:
        result = func(item)
        if result not in dictionary:
            dictionary[result] = [item]
        else:
            dictionary[result].append(item)
    return dictionary
