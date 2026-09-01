"""unique number"""
s, e = map(int, input().split())
prime_l = []

for i in range(s, e + 1):
    if i <= 1:
        continue
    for j in range(2, i):
        if not i % j:
            break
    else:
        prime_l.append(i)

if len(prime_l) > 0:
    print(*prime_l)
print(f"Total primes: {len(prime_l)}")
