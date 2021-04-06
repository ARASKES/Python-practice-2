message = input()
letter_number = int(input())
fav_letter = input()

if not 1 <= letter_number <= len(message) or len(fav_letter) > 1:
    print("ОШИБКА")
elif message[letter_number - 1] == fav_letter:
    print("ДА")
else:
    print("НЕТ")
