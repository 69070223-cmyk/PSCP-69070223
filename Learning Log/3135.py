"""wtf"""
n, k, t = map(int, input().split())
current = 1
count = 1
if t == 1:
    print(1)
else:
    while True:
        current = (current + k - 1) % n + 1

        if current == 1:
            break

        count += 1

        if current == t:
            break

    print(count)
