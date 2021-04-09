N = int(input())
score_table = {}
for i in range(N):
    key = input()
    value = int(input())
    score_table[key] = value

sorted_table = sorted(score_table.items(), key=lambda x: x[1])
finalists = []
non_finalists = []
finalists_quantity = len(sorted_table) // 2
for i in range(len(sorted_table)):
    if i < finalists_quantity:
        non_finalists.append(sorted_table[i])
    else:
        finalists.append(sorted_table[i])

finalists_names = []
for finalist in finalists:
    finalists_names.append(finalist[0])
finalists_names.sort()

non_finalists_names = []
for non_finalist in non_finalists:
    non_finalists_names.append(non_finalist[0])
non_finalists_names.sort()

for fn in finalists_names:
    print(fn)
for nfn in non_finalists_names:
    print(nfn)
