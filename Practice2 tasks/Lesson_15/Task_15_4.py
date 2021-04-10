def most_frequent(numbers):
    most_frequent_element = 0
    max_count = 0
    for element in numbers:
        count = 0
        for el in numbers:
            if el == element:
                count += 1
        if count > max_count:
            max_count = count
            most_frequent_element = element

    return most_frequent_element


N = int(input())
lines = []
for i in range(N):
    lines.append(input())

rows = []
for line in lines:
    row = []
    number = ""
    for char in line:
        if char == " ":
            row.append(int(number))
            number = ""
        else:
            number += char
    row.append(int(number))
    row.sort()
    rows.append(row)

medians = []
for row in rows:
    median = row[len(row) // 2]
    medians.append(median)
    print(median, end=" ")
print()

modes = []
for row in rows:
    mode = most_frequent(row)
    modes.append(mode)
    print(mode, end=" ")
print()

medians.sort()
print(medians[len(medians) // 2])

print(most_frequent(modes))

rows_united = []
for row in rows:
    for number in row:
        rows_united.append(number)
rows_united.sort()

print(rows_united[len(rows_united) // 2])

print(most_frequent(rows_united))
