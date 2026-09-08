"""lottery"""
T, NUM = map(str, input().split())
t, num = map(str, input().split())
reward = 0
if T == t:
    if NUM == num:
        reward = 1000000
    elif NUM[-3] == num[-3]:
        reward = max(reward,2000)
    elif NUM[-2] == num[-2]:
        reward = max(reward,1000)
    else:
        reward = 20
else:
    if NUM == num:
        reward = 100000
    elif NUM[-3] == num[-3]:
        reward = max(reward,200)
    elif NUM[-2] == num[-2]:
        reward = max(reward,100)
    else:
        reward = 0

print(reward)
