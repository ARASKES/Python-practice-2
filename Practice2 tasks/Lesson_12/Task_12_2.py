N = ""
summary = ""
first_line = input()
for i in range(len(first_line)):
    if i < 3:
        N += first_line[i]
    elif i > 3:
        summary += first_line[i]
N = int(N)
summary = int(summary)

check_lines = []
for i in range(N):
    check_lines.append(input())

mistakes = []
real_summary = 0
for i in range(len(check_lines)):
    price = ""
    multiplier = ""
    line_sum = ""
    for j in range(len(check_lines[i])):
        if check_lines[i][j].isdigit():
            if j < 6:
                price += check_lines[i][j]
            elif 7 < j < 11:
                multiplier += check_lines[i][j]
            elif j > 11:
                line_sum += check_lines[i][j]
    price = int(price)
    multiplier = int(multiplier)
    line_sum = int(line_sum)

    real_summary += price * multiplier
    if line_sum != price * multiplier:
        mistakes.append(i + 1)

dif = abs(real_summary - summary)
print(dif)
if dif > 0:
    for mistake in mistakes:
        print(mistake, end=" ")
