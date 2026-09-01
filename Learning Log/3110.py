"""santi"""
s, e = input().split()
w = float(input())
fee = 0
feew = 0
check = 0
if s == "BKK" and e == "CNX":
    fee = 10
    feew = 30
    check = 1
elif s == "CNX" and e == "UBP":
    fee = 15
    feew = 40
    check = 1
elif s == "UBP" and e == "BKK":
    fee = 20
    feew = 40
    check = 1
elif s == "BKK" and e == "PKT":
    fee = 25
    feew = 50
    check = 1
elif s == "PKT" and e == "CNX":
    fee = 30
    feew = 60
    check = 1
elif s == "UBP" and e == "PKT":
    fee = 40
    feew = 70
    check = 1

if check == 1:
    price = fee+(feew*w)
    print(f"{price:.2f}")
else:
    print("Error")