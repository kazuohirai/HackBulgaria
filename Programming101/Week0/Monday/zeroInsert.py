from listToNum import list_to_number


def zero_insert(n):
    num = list(str(n))
    count = len(num) - 1
    index = len(num) - 1
    for k in range(0, len(num) - 1):
        if n % 10 == (n / 10) % 10 or (n % 10 + (n / 10 % 10)) % 10 == 0:
            num.append(num[count])
            count += 1
            temp1 = ""
            temp2 = num[index]
            for i in range(index + 1, count):
                temp1 = num[i]
                num[i] = temp2
                temp2 = temp1
            num[index] = "0"
        index -= 1
        n /= 10
    return list_to_number(num)
