n = int(input())
field = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    field.append(row)

k = int(input())
for i in range(k):
    x = int(input())
    y = int(input())

    field[y][x] -= 4
    for j in range(n):
        for m in range(n):
            if (y - 1 <= j <= y + 1) and (x - 1 <= m <= x + 1):
                field[j][m] -= 4

                if field[j][m] < 0:
                    field[j][m] = 0

for row in field:
    for bacteria in row:
        print(bacteria, end=" ")
    print()
