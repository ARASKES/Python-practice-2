# Мой формат "CSV 2.0" предполагает использование символа "\"
# перед символами "," и "n" для добавления в ячейку запятой и
# перехода на новую строку соответственно. Для добавления символа
# "\" необходимо использовать комбинацию "\\".

R = int(input())
lines = []
for i in range(R):
    lines.append(input())

table = []
for line in lines:
    words = []
    word = ""
    for i in range(len(line)):
        if line[i] == "\\":
            if line[i - 1] == "\\":
                word += "\\"
        elif line[i] == ",":
            if line[i - 1] == "\\":
                word += ","
            else:
                words.append(word)
                word = ""
        elif line[i] == "n" and line[i - 1] == "\\":
            word += "\n"
        else:
            word += line[i]
    words.append(word)

    table.append(words)

N = int(input())
coordinates = []
for i in range(N):
    coords = input()
    row = ""
    column = ""
    was_comma_encountered = False
    for char in coords:
        if char == ",":
            was_comma_encountered = True
        else:
            if was_comma_encountered:
                column += char
            else:
                row += char
    coordinates.append((int(row), int(column)))

for coords in coordinates:
    print(table[coords[0]][coords[1]])
