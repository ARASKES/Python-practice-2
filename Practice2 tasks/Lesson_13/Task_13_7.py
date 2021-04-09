N = int(input())
soldiers = []
for i in range(N):
    soldiers.append(input())
K = int(input())

initial_length = len(soldiers)
executed = 0
while len(soldiers) > 0:
    to_remove = []
    for i in range(0, len(soldiers), K):
        soldier = soldiers[i]
        print(soldier)
        to_remove.append(soldier)
        executed += 1
    for removed in to_remove:
        soldiers.remove(removed)
