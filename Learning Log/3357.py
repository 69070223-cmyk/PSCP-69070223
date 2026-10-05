"""gi"""
n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

answer = 0
if n == 1:
    print(1)
else:
    for i in range(n):
        if not i:
            if a[i] > a[i + 1]:
                answer += 1

        elif i == n - 1:
            if a[i] > a[i - 1]:
                answer += 1

        else:
            if a[i] > a[i - 1] and a[i] > a[i + 1]:
                answer += 1

    print(answer)
