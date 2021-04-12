tape = []
for i in range(30000):
    tape.append(0)
carriage_index = 0

commands = input()

brackets = {}
for i in range(len(commands)):
    if commands[i] == "[":
        count = 0
        for j in range(i + 1, len(commands)):
            if commands[j] == "[":
                count += 1
            elif commands[j] == "]":
                if count == 0:
                    brackets[i] = j
                else:
                    count -= 1

i = 0
while i < len(commands):
    if commands[i] == ">":
        if carriage_index == len(tape) - 1:
            carriage_index = 0
        else:
            carriage_index += 1
    elif commands[i] == "<":
        if carriage_index == 0:
            carriage_index = len(tape) - 1
        else:
            carriage_index -= 1
    elif commands[i] == "+":
        tape[carriage_index] += 1
        tape[carriage_index] %= 256
    elif commands[i] == "-":
        tape[carriage_index] -= 1
        tape[carriage_index] %= 256
    elif commands[i] == ".":
        print(tape[carriage_index])
    elif commands[i] == "[":
        if tape[carriage_index] == 0:
            if brackets.get(i) == len(commands) - 1:
                break
            else:
                i = brackets.get(i)
    elif commands[i] == "]":
        for key, value in brackets.items():
            if value == i:
                i = key - 1
                break

    i += 1
