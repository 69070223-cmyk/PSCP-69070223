"""pasthai"""
allowed_ingredients = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip",
    "Shrimp", "Bean Sprouts", "Noodle", "Chives",
    "Lime", "Egg", "Oil", "Peanuts"
}

required_flavors = {"Sweet", "Sour", "Salty"}

ingredients = set()
while True:
    item = input()
    if item == "Cook":
        break
    ingredients.add(item)

flavors = set()
while True:
    flavor = input()
    if flavor == "End":
        break
    flavors.add(flavor)

if ingredients - allowed_ingredients:
    print("This is not Pad Thai!!!")
elif allowed_ingredients - ingredients:
    print("This is bad!")
elif not allowed_ingredients - ingredients:
    if required_flavors - flavors or flavors - required_flavors:
        print("Not Bad...")
    else:
        print("Delicious!")
