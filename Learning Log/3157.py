"""action"""
n = int(input())
point= 0
for _ in range(n):
    a = input()
    if a == "+":
        point += 10
    else:
        point -= 5

print(point)
