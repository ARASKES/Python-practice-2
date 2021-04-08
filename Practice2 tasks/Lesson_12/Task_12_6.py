A = [
    "    *    ",
    "   * *   ",
    "  *   *  ",
    " ******* ",
    "*       *"
]
B = [
    "**** ",
    "*   *",
    "* ** ",
    "*   *",
    "**** "
]
C = [
    " *** ",
    "*   *",
    "*    ",
    "*   *",
    " *** "
]

text = input()
output = []
for symbol in text:
    if symbol == "A":
        output.append(A)
    elif symbol == "B":
        output.append(B)
    elif symbol == "C":
        output.append(C)
for j in range(5):
    for i in range(len(output)):
        print(output[i][j], end="  ")
    print()
