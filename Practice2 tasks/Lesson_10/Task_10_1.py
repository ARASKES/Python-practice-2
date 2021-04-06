message = input()
letter_number = int(input())

if 1 <= letter_number <= len(message):
    print(message[letter_number - 1])
else:
    print("ОШИБКА")
