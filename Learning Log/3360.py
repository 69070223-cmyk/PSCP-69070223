"""kanompang"""
w, h, _, _ = map(int, input().split())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

width = []
previous = 0

for i in x:
    width.append(i - previous)
    previous = i

width.append(w - previous)

height = []
previous = 0

for i in y:
    height.append(i - previous)
    previous = i

height.append(h - previous)

width.sort(reverse=True)
height.sort(reverse=True)

area1 = width[0] * height[0]
area2 = max(width[0] * height[1], width[1] * height[0])

print(area1, area2)
