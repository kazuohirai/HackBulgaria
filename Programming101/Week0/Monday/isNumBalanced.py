def is_number_balanced(n):
    temp = str(n)
    if len(temp) == 1:
        return True
    else:
        left = ""
        right = ""
        for i in range(0, len(temp) / 2):
            left += temp[i]
        temp = temp[::-1]
        for i in range(0, len(temp) / 2):
            right += temp[i]
        right = right[::-1]
        ileft = int(left)
        iright = int(right)
        sleft = 0
        sright = 0
        for i in range(0, len(left)):
            sleft += ileft % 10
            ileft /= 10
        for i in range(0, len(right)):
            sright += iright % 10
            iright /= 10
        if sright == sleft:
            return True
        return False
