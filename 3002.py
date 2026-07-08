"""Cyan pass"""
name = input()
surname = input()
age = int(input())

if len(name) > 5:
    print(name[:2] + surname[-1] + str(age)[-1])
else:
    print(name[:1] + str(age) + surname[-1])
