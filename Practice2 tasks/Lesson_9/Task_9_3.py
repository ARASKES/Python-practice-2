N = int(input())
surnames = []
for i in range(N):
    surnames.append(input())
black_list = []

namesakes = 0
for i in range(len(surnames)):
    if black_list.__contains__(surnames[i]):
        continue
    matches = 0
    for j in range(len(surnames)):
        if i == j:
            continue
        if surnames[i] == surnames[j]:
            matches += 1
    if matches > 0:
        namesakes += matches + 1

    black_list.append(surnames[i])

print(namesakes)
