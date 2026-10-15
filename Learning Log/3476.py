"""fubuki"""
import ast
n = int(input())
cats = {}
foxes = {}

for _ in range(n):
    data = ast.literal_eval(input())

    for name, code in data.items():
        if code.startswith("Cat"):
            cats[code] = name
        elif code.startswith("Fox"):
            foxes[code] = name

if "Garfield" not in cats.values() and "Cat01" not in cats and "Garfield" not in foxes.values():
    cats["Cat01"] = "Garfield"

if "Fubuki" not in foxes.values() and "Fox01" not in foxes and "Fubuki" not in cats.values():
    foxes["Fox01"] = "Fubuki"

print(f"Cat : {len(cats)}")
print(f"Fox : {len(foxes)}")

for code in sorted(cats, key=lambda x: int(x[3:])):
    print(f"{cats[code]} : {code}")

for code in sorted(foxes, key=lambda x: int(x[3:])):
    print(f"{foxes[code]} : {code}")
