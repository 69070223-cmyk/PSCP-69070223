"""sahagon"""
import math
mem = input()
n = int(input())
item = 0
for i in range(n):
    item += float(input())

if mem == "Y":
    item = (item)*0.95
elif item >= 500:
    item = (item)*0.97
item = math.ceil(item*100)
print(f"{item/100:.2f}")
