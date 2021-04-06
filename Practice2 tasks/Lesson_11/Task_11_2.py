N = int(input())
lines = []
for i in range(N):
    lines.append(input())

for i in range(N):
    if lines[i].startswith("%%"):
        for j in range(2, len(lines[i])):
            print(lines[i][j], end="")
    elif lines[i].startswith("####"):
        continue
    else:
        print(lines[i])
