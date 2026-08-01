import os

file_path = os.path.join(os.getcwd(), "recipe.txt")

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

omelet = lines[0].strip()
dack = lines[6].strip()
potato = lines[13].strip()
fajitas = lines[19].strip()

def ingredients(name):
    ingredients = []
    if name == dack:
        x = 8
        y = x + int(lines[7]) - 1
    elif name == omelet:
            x = 2
            y = x + int(lines[1]) - 1
    elif name == potato:
            x = 15
            y = x + int(lines[14]) - 1
    elif name == fajitas:
            x = 21
            y = x + int(lines[20]) - 1
    while x <= y :
        ing = lines[x].strip().split("|")
        ingredients_name = ing[0]
        quantity = ing[1]
        measure = ing[2]
        x += 1
        ingredients.append({'ingredient_name': ingredients_name, 'quantity': quantity, 'measure': measure})
    return ingredients

cook_book = {omelet: ingredients(omelet), dack: ingredients(dack), potato: ingredients(potato), fajitas: ingredients(fajitas)}

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                ingredient['quantity'] = int(ingredient['quantity']) * person_count
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity']}
            else:
                ingredient['quantity'] = int(ingredient['quantity']) * person_count + shop_list[ingredient['ingredient_name']]['quantity']
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity']}
    return shop_list

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 6))