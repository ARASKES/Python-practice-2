nums = input()
numbers = []
number = ""
for char in nums:
    if char == " ":
        numbers.append(int(number))
        number = ""
    else:
        number += char
numbers.append(int(number))

diagram_height = max(numbers) + 2
for i in range(diagram_height):
    if i == 0:
        for j in range(len(numbers) + 2):
            print("*", end="")
    elif i == 1:
        for j in range(len(numbers) + 2):
            if j == 0 or j == len(numbers) + 1:
                print("*", end="")
            else:
                print(" ", end="")
    else:
        for j in range(len(numbers) + 2):
            if j == 0 or j == len(numbers) + 1:
                print("*", end="")
            else:
                if diagram_height - i <= numbers[j - 1]:
                    print("*", end="")
                else:
                    print(" ", end="")
    print()
