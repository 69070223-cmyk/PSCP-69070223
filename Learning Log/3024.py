"""surprise matafaka"""
total = float(input())
high = float(input())
low = 0
other = total - high
text = ""

if other >= high:
    low = total - (high * 2)
elif other < high:
    low = 0

if high - low > 2:
    text = "Surprising"
else:
    text = "Not surprising"

print(text)
