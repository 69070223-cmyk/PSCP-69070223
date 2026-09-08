"""frog"""
x, y = map(int, input().split())
po = 0
n = 0
while po < y and x > 0:
    po += x
    x -= 2
    n += 1

if po >= y:
    print(n)
else:
    print(-1)
