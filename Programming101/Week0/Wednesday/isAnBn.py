def is_an_bn(word):
    index = 0
    count = 0
    if len(word) < 1:
        return True
    while index < len(word):
        if word[index] == 'a' and count >= 0:
            count += 1
        if word[index] == 'b' and count > 0:
            count -= 1
        index += 1
    for i in range(0, len(word) - 1):
        if word[i] == "b" and word[i + 1] == "a":
            return False
    if count == 0:
        return True
    return False
