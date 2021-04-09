S = int(input())
brothers_chars = []
chars = []
for i in range(S):
    chars.append(int(input()))
for i in range(2):
    bc = []
    for j in range(S):
        bc.append(chars[j])
    brothers_chars.append(bc)

N = int(input())
for i in range(N):
    brother = int(input()) - 1
    char = int(input())
    brothers_chars[brother][char] += int(input())

for bro in brothers_chars:
    for char in bro:
        print(char, end=" ")
    print()

coincidences = 0
for i in range(S):
    if brothers_chars[0][i] == brothers_chars[1][i]:
        coincidences += 1
print(coincidences)
