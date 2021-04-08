n = int(input())
fraction = (1 / n).__str__()
fraction = fraction[2: -1:][0: 16:][:: -1]

max_period = ""
for step in range(1, len(fraction) // 2):
    period = ""
    if step > 1:
        period = fraction[0: step:]
    else:
        period = fraction[0]
    is_repeating = True
    for i in range(0, len(fraction), step):
        for j in range(i, i + step):
            if j < len(fraction):
                if period[j - i] != fraction[j] and j < len(fraction) - step:
                    is_repeating = False
    if is_repeating:
        max_period = period
        break

if len(fraction) < 15:
    max_period = "0"

are_digits_same = True
for digit in max_period:
    are_digits_same *= digit == max_period[0]
if are_digits_same:
    max_period = max_period[0]

print(max_period[:: -1])
