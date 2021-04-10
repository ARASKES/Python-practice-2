line = input()

count = 0
for char in line:
    if char != " " and char != "\t":
        count += 1
print(count)
