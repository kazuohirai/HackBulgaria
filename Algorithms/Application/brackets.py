def outermost_brackets(word):
    open = ['(', '[', '{']
    close = [')', ']', '}']
    if word[0] in open and word[-1] == close[open.index(word[0])]:
        return True
    return False


def normal_contents(word):
    if '(' not in word and ')' not in word:
        return True
    start = word.find('(')
    end = word[::-1].find(')')
    end = len(word) - end
    if (start == -1 and end != -1) or (start != -1 and end == -1):
        return False
    if end < start:
        return False
    check = word[start:end]
    error = ['[', ']', '{', '}']
    for each in error:
        if each in check:
            return False
    return True


def nested(word):
    opening = word[0]
    for i in range(1, len(word) - 1):
        if word[i] == opening:
            return False
    return True


def square_brackets(word):
    if '[' not in word and ']' not in word:
        return True
    start = word.find('[')
    for i in range(start, len(word)):
        if word[i] == '{':
            return False
    return True


def curly_brackets(word):
    if '{' in word and '}' in word:
        if not ('[' in word and ']' in word):
            if '(' in word and ')' in word:
                return False
            return True
        return True
        in_squares = False
        for each in word:
            if each == '[':
                in_squares = True
            if each == '(' and in_squares:
                return True
        return False
    return True


def validate(word):
    return (outermost_brackets(word) and normal_contents(word)
            and nested(word) and square_brackets(word)
            and curly_brackets(word))


def trimmer(word):
    word = word.replace('+)', '+0)')
    word = word.replace('()', '(0)')
    return word


def all_brackets(word):
    word = word.replace('(', '+2*(')
    word = word.replace(')', ')+')
    word = word.replace('[', '+2*(')
    word = word.replace(']', ')+')
    word = word.replace('{', '(')
    word = word.replace('}', ')+')
    word = trimmer(word)
    return word[:-1].replace('++', '+')


def curly_and_square(word):
    word = word.replace('[', '+2*(')
    word = word.replace('{', '(')
    word = word.replace(']', ')+')
    word = word.replace('}', ')+')
    word = trimmer(word)
    return word[:-1].replace('++', '+')


def square_normal(word):
    word = word.replace('(', '+2*(')
    word = word.replace(')', ')+')
    word = word.replace('[', '(')
    word = word.replace(']', ')+')
    word = trimmer(word)
    return word[:-1].replace('++', '+')


def normal_only(word):
    return word


def square_only(word):
    word = word.replace('[', '(')
    word = word.replace(']', ')')
    return word


def curly_only(word):
    word = word.replace('{', '(')
    word = word.replace('}', ')')
    return word


def prepare(word):
    equation = ''
    for each in word:
        equation += each
    if '[' in equation and ']' in equation:
        if '{' in equation and '}' in equation:
            if not ('(' in equation and ')' in equation):
                return curly_and_square(equation)
            if '(' in equation and ')' in equation:
                return all_brackets(equation)
        if not ('{' in equation and '}' in equation):
            if not ('(' in equation and ')' in equation):
                return square_only(equation)
            if '(' in equation and ')' in equation:
                return square_normal(equation)
    if not ('[' in equation and ']' in equation):
        if '{' in equation and '}' in equation:
            return curly_only(equation)
        if '(' in equation and ')' in equation:
            return normal_only(equation)


def calculate(word):
    if validate(word):
        return eval(prepare(word))
    else:
        return 'NO'
