N = int(input())
contacts = {}
for i in range(N):
    words = input().split(" ")
    if not contacts.keys().__contains__(words[1]):
        contacts[words[1]] = []
    contacts.get(words[1]).append(words[0])

M = int(input())
for i in range(M):
    request = input()
    if contacts.keys().__contains__(request):
        phone_numbers = contacts.get(request)
    else:
        print("Нет в телефонной книге")
        continue
    for pn in phone_numbers:
        print(pn, end=" ")
    print()
