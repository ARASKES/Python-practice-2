def is_big_cyrillic(symbol):
    return 1040 <= ord(symbol) <= 1071


def is_small_cyrillic(symbol):
    return 1072 <= ord(symbol) <= 1103


ALPHABET_LENGTH = 32    # Длина алфавита 32, потому что мы не учитываем букву "ё"

step = int(input()) % ALPHABET_LENGTH
message = input()
ciphered_message = ""

for symb in message:
    if is_big_cyrillic(symb):
        ciphered_message += chr(1040 + (ord(symb) + step - 1040) % ALPHABET_LENGTH)
    elif is_small_cyrillic(symb):
        ciphered_message += chr(1072 + (ord(symb) + step - 1072) % ALPHABET_LENGTH)
    else:
        ciphered_message += symb

print(ciphered_message)
