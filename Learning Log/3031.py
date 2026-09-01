"""ink"""
import math
s, n = map(int, input().split())

for i in range(n):
    x, y = map(int, input().split())
    area = 3.1416 * (x ** 2 + y** 2)
    t = area / s
    print(math.ceil(t))
