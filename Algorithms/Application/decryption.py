def get_alphabet(msg):
    AB_len = ''
    alphabet = ''
    for i in range(msg.find('~')):
        AB_len += msg[i]
    for i in range(0, int(AB_len)):
        alphabet += msg[int(msg.find('~')) + 1 + i]
    return alphabet


def get_key(msg):
    key_len = ''
    key = ''
    rev = msg[::-1]
    for i in range(msg.find('~') - 1):
        key_len += rev[i]
    key_len = int(key_len[::-1])
    for i in range(0, key_len):
        key += rev[int(rev.find('~')) + 1 + i]
    return key[::-1]


def get_encrypted(msg, alphabet, key):
    index = msg.find(alphabet) + len(alphabet)
    message = ''
    for i in range(index, msg.find(key)):
        message += msg[i]
    return message


def get_alphabet_indices(text, alphabet):
    indices = []
    for item in text:
        indices.append(alphabet.find(item))
    return indices


def construct_compound_key(msg_len, key):
    compound = ''
    for i in range(0, msg_len, len(key)):
        compound += key
    return compound[:msg_len]


def get_indices_of_actual_msg(encrypted, compound, alphabet):
    encr_indices = get_alphabet_indices(encrypted, alphabet)
    comp_indices = get_alphabet_indices(compound, alphabet)
    for i in range(0, len(encr_indices)):
        encr_indices[i] = (
            encr_indices[i] + len(alphabet) - comp_indices[i]) % len(alphabet)
    return encr_indices


def decrypt(msg):
    actual = msg[len(msg) // 2:] + msg[:len(msg) // 2]
    alphabet = get_alphabet(actual)
    key = get_key(actual)
    encrypted = get_encrypted(actual, alphabet, key)
    compound = construct_compound_key(len(encrypted), key)
    actual_indices = get_indices_of_actual_msg(encrypted, compound, alphabet)
    message = ""
    for item in actual_indices:
        message += alphabet[item]
    return message
