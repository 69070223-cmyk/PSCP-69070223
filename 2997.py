""" Elo """
ea = int(input())
eb = int(input())
typeofqua = input()

if typeofqua == "A":
    result = 1 / (1 + 10 ** ((eb - ea)/400) )
else:
    result = 1 / (1 + 10 ** ((ea - eb)/400) )

print((f"{result:.2f}"))
