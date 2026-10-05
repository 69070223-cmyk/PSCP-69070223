"""songtor"""
n, s = map(int, input().split())

send = [0]

for _ in range(n):
    send.append(int(input()))

visited = set()
current = s

while current and current not in visited:
    visited.add(current)
    current = send[current]

print(len(visited))
