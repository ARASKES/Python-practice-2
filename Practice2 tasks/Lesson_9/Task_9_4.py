products_available = []
M = int(input())
for i in range(M):
    products_available.append(input())

recipes = {}
N = int(input())
for i in range(N):
    recipe_name = input()
    ingredients_count = int(input())
    ingredients = []
    for j in range(ingredients_count):
        ingredients.append(input())
    recipes[recipe_name] = ingredients

for key in recipes.keys():
    can_be_cooked = True
    for i in recipes[key]:
        can_be_cooked *= products_available.__contains__(i)
    if can_be_cooked:
        print(key)
