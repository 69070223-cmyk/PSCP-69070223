"""sapan"""
numa = int(input())
numb = int(input())
goal = int(input())

a = 1
b = 5

if (numa * a) + (numb * b) >= goal:
    numb = min(numb, goal // b)
    goal -= numb * b
    a = goal // a
    if a <= numa:
        print(int(a))
    else:
        print(-1)

else:
    print(-1)
