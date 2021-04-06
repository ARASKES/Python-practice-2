command = input()

drawing_symbol = command[0]
last_line = ""
for i in range(len(command)):
    if command[i] == "<":
        new_line = ""
        for j in range(len(last_line)):
            if last_line[j] == drawing_symbol or j != len(last_line) - 1 and last_line[j + 1] == drawing_symbol:
                new_line += drawing_symbol
            else:
                new_line += last_line[j]
        last_line = new_line
    elif command[i] == ">" or i == 0:
        last_line += drawing_symbol
    elif command[i] == "V":
        print(last_line)
        new_line = ""
        for j in range(len(last_line)):
            if last_line[0] == " " and last_line[j] == drawing_symbol \
                    or last_line[0] == drawing_symbol and j == len(last_line) - 1:
                new_line += drawing_symbol
                break
            else:
                new_line += " "
        last_line = new_line
print(last_line)
