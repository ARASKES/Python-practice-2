N = int(input())
sequence = []
for i in range(N):
    if i == 0:
        sequence.append(0)
    else:
        coincidences = 0
        for j in range(len(sequence)):
            if sequence[j] == sequence[-(j + 1)]:
                coincidences += 1
        sequence.append(coincidences)

for member in sequence:
    print(member)
