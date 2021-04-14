def transliterate(cyrillic):
    if cyrillic == "а":
        return "a"
    elif cyrillic == "б":
        return "b"
    elif cyrillic == "в":
        return "v"
    elif cyrillic == "г":
        return "g"
    elif cyrillic == "д":
        return "d"
    elif cyrillic == "е" or cyrillic == "ё" or cyrillic == "э":
        return "e"
    elif cyrillic == "ж":
        return "zh"
    elif cyrillic == "з":
        return "z"
    elif cyrillic == "и" or cyrillic == "й":
        return "i"
    elif cyrillic == "к":
        return "k"
    elif cyrillic == "л":
        return "l"
    elif cyrillic == "м":
        return "m"
    elif cyrillic == "н":
        return "n"
    elif cyrillic == "о":
        return "o"
    elif cyrillic == "п":
        return "p"
    elif cyrillic == "р":
        return "r"
    elif cyrillic == "с":
        return "s"
    elif cyrillic == "т":
        return "t"
    elif cyrillic == "у":
        return "u"
    elif cyrillic == "ф":
        return "f"
    elif cyrillic == "х":
        return "kh"
    elif cyrillic == "ц":
        return "tc"
    elif cyrillic == "ч":
        return "ch"
    elif cyrillic == "ш":
        return "sh"
    elif cyrillic == "щ":
        return "shch"
    elif cyrillic == "ы":
        return "y"
    elif cyrillic == "ю":
        return "iu"
    elif cyrillic == "я":
        return "ia"


text = input()

transliterated = ""
for letter in text:
    if letter == "ь" or letter == "ъ" or letter == "Ь" or letter == "Ъ":
        continue
    elif "а" <= letter <= "я":
        transliterated += transliterate(letter.lower())
    elif "А" <= letter <= "Я":
        transliterated += transliterate(letter.lower()).capitalize()
    else:
        transliterated += letter

print(transliterated)
