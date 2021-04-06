N = int(input())

lines = []
for i in range(N):
    line = input()

    formatted_line = ""
    isQuoted = False
    for j in range(len(line)):
        if not isQuoted and line[j] == '\'' or line[j] == '\"':
            isQuoted = True
        elif isQuoted and line[j] == '\'' or line[j] == '\"' and \
                (line[j - 1] != '\\' or line[j - 1] == '\\' and line[j - 2] == '\\'):
            isQuoted = False

        if line[j] == " " and line[j + 1] == " " and j != len(line) - 1 and not isQuoted:
            continue
        elif line[j] == "#" and not isQuoted:
            break
        else:
            formatted_line += line[j]
    lines.append(formatted_line)
for ln in lines:
    print(ln)
