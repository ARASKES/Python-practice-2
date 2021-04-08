digits = input()

new_digit = ""
count = 0
for digit in digits:
    if digit != new_digit:
        print(count, new_digit)
        new_digit = digit
        count = 1
    else:
        count += 1
print(count, new_digit)
