"""prasat"""
import math

n = int(input())

row = math.ceil(math.sqrt(n))
position = n - ((row - 1) ** 2)

if position % 2 == 1:
    ans = 2 * (row - 1)
else:
    ans = 2 * row - 3

print(ans)
