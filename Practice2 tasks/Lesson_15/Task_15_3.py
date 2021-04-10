line = input().lower()

max_entries = 0
count = 0
for char in line:
    for character in line:
        if character == char:
            count += 1

    if count > max_entries:
        max_entries = count
    count = 0

print(max_entries)
