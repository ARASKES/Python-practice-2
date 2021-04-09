N = int(input())
recipe = ""
for i in range(N):
    line = input()
    if not line.__contains__("лук"):
        recipe += line + ", "
print(recipe)
