""":-:"""
a = int(input())
b = int(input())
d = int(input())
r = int(input())

ans = 0
for i in range(a, b + 1):
    if i % d == r:
        ans += 1

print(ans)
