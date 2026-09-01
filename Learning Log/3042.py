"""han 10"""
num = int(input())
number = num // 10
lekk = []

for i in range(number + 1):
    lekk.append(i * 10)

print(*lekk[::-1])
