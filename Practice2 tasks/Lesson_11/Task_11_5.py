def bite(word):
    bitten_word = ""
    for i in range(len(word)):
        if i != 0 and i != len(word) - 1:
            bitten_word += word[i]
    return bitten_word


word_to_bite = input()
while len(word_to_bite) > 2:
    word_to_bite = bite(word_to_bite)
    print(word_to_bite)
