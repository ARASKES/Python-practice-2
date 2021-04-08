N = 2 * int(input())
purchase_list = []
for i in range(N):
    purchase_list.append(input())

i = N - 1
while i > 0:
    print(purchase_list[i - 1], purchase_list[i])
    i -= 2
