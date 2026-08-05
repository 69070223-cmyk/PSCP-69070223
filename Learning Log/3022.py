"""temp change"""
temp = float(input())
current = input()
need = input()

if current == "C":
    if need == "C":
        temp = temp
    elif need == "K":
        temp = temp + 273.15
    elif need == "F":
        temp = (temp * 9 / 5) + 32
    elif need =="R":
        temp = (temp + 273.15) * 9 / 5
elif current == "K":
    if need == "C":
        temp = temp - 273.15
    elif need == "K":
        temp = temp
    elif need == "F":
        temp = (temp - 273.15) * 9 / 5 + 32
    elif need =="R":
        temp = temp * 9 / 5  
elif current == "F":
    if need == "C":
        temp = (temp - 32) * 5 / 9
    elif need == "K":
        temp = (temp - 32) * 5 / 9 + 273.15
    elif need == "F":
        temp = temp
    elif need =="R":
        temp = temp + 459.67
elif current == "R":
    if need == "C":
        temp = (temp - 491.67) * 5 / 9
    elif need == "K":
        temp = temp * 5 / 9
    elif need == "F":
        temp = temp - 459.67
    elif need =="R":
        temp = temp

print(f"{temp:.2f}")
