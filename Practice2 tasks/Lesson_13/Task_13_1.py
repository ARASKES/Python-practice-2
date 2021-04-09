n = int(input())
items = []
for i in range(n):
    items.append(input())

k = int(input())
for i in range(k):
    quantity = int(input())
    items_moved = []
    for j in range(quantity):
        items_moved.append(items[int(input()) - 1])
    items = items_moved

for item in items:
    print(item)
