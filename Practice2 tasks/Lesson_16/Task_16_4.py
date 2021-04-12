N = int(input())
table = []
M = 0
if N % 2 == 0:
    M = N // 2
else:
    M = N // 2 + 1

half_a_table = []
for i in range(M):
    line = input()
    number = ""
    for symbol in line:
        if symbol == " ":
            half_a_table.append(int(number))
            number = ""
        else:
            number += symbol
    half_a_table.append(number)

number_index = 0
for i in range(N):
    line = []
    for j in range(N):
        if j >= i:
            line.append(0)
        else:
            line.append(int(half_a_table[number_index]))
            number_index += 1
    table.append(line)

stations = input()
depart = ""
dest = ""
number = ""
for symbol in stations:
    if symbol == " ":
        depart = int(number)
        number = ""
    else:
        number += symbol
dest = int(number)

if depart > dest:
    straight = table[depart][dest]
else:
    straight = table[dest][depart]

shortest = straight
station = 0
for i in range(1, N):
    if depart == 0:
        non_straight = table[i][depart] + table[i][dest]
    else:
        non_straight = table[depart][i] + table[i][dest]
    if non_straight < shortest:
        shortest = non_straight
        station = i

print(station)
