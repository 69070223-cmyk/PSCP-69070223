"""dupl"""
m = int(input())
n = int(input())

A = set()
B = set()

for _ in range(m):
    A.add(int(input()))

for _ in range(n):
    B.add(int(input()))

answer = sorted(A & B, reverse=True)

if not answer:
    print("Nope")
else:
    print(*answer, sep="\n")
