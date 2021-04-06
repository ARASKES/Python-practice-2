sequence = input()

max_heads = 0
heads_in_a_row = 0
for throw in sequence:
    if throw == 'о':
        heads_in_a_row += 1
    else:
        heads_in_a_row = 0

    if heads_in_a_row > max_heads:
        max_heads = heads_in_a_row
print(max_heads)
