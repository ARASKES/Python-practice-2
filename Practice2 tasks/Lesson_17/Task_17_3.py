N = int(input())
birthdays = {}
for i in range(N):
    words = input().split(" ")
    if not birthdays.keys().__contains__(words[2]):
        birthdays[words[2]] = []
    birthdays.get(words[2]).append((words[0], words[1]))

M = int(input())
for i in range(M):
    request = input()
    if birthdays.keys().__contains__(request):
        names_n_days = birthdays.get(request)
    else:
        print()
        continue
    for name, day in names_n_days:
        print(name, day, sep=" ", end=" ")
    print()
