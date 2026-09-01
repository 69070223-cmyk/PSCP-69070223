"""aeiou"""
t = input().lower()
vowels = ["a", "e", "i", "o", "u"]
count = [0, 0, 0, 0, 0]

for i in t:
    if i in vowels:
        x = vowels.index(i)
        count[x] += 1

for i in range(5):
    if count[i] >= 1:
        print(f"{vowels[i]} : {count[i]}")
