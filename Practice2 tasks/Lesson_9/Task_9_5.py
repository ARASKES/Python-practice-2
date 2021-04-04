dishes_available = []
M = int(input())
for i in range(M):
    dishes_available.append(input())

last_days_lists = []
N = int(input())
for i in range(N):
    dishes = []
    dishes_count = int(input())
    for j in range(dishes_count):
        dishes.append(input())
    last_days_lists.append(dishes)

for dish in dishes_available:
    was_not_cooked = True
    for cooked_dishes in last_days_lists:
        was_not_cooked *= not cooked_dishes.__contains__(dish)
    if was_not_cooked:
        print(dish)
