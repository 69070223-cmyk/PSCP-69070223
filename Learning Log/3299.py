"""flowerpot"""
l, n = map(int, input().split())
pot = 0
band = 0
diagonal = 0

while pot < n:
    band += 1

    for _ in range(l):
        diagonal += 1
        pot += diagonal

print(band)
