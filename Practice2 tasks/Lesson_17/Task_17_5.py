N = int(input())
resolutions = []
for i in range(N):
    resolutions.append(input())

M = int(input())
requests = []
for i in range(M):
    request = input()

    response = "NO"
    for res in resolutions:
        if len(res) <= len(request) and request[0: len(res):] == res:
            response = "YES"
    print(response)
