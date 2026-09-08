"""cards"""
t = input().upper()

values = {
    "A" : "ace",
    "K" : "king",
    "Q" : "queen",
    "J" : "jack"
}

classs = {
    "H" : "hearts",
    "D" : "diamonds",
    "S" : "spades",
    "C" : "clubs"
}

v = t[:-1]
c = t[-1]
v = values.get(v, v)

print(f"{v} of {classs[c]}")
