"""tile"""
n, p = input().split()
n = int(n)
p = float(p)

tiles = []
for _ in range(n):
    tiles.append(list(map(int, input().split())))

total_tiles = 0
total_points = 0

row_bad_tiles = []
row_bad_points = []

for i in range(n):
    bad_tiles = 0
    bad_points = 0

    for j in range(n):
        if tiles[i][j] > 0:
            bad_tiles += 1
            bad_points += tiles[i][j]

    total_tiles += bad_tiles
    total_points += bad_points
    row_bad_tiles.append(bad_tiles)
    row_bad_points.append(bad_points)

    print(*tiles[i], bad_tiles, bad_points)

col_bad_tiles = []
col_bad_points = []

for j in range(n):
    bad_tiles = 0
    bad_points = 0

    for i in range(n):
        if tiles[i][j] > 0:
            bad_tiles += 1
        bad_points += tiles[i][j]

    col_bad_tiles.append(bad_tiles)
    col_bad_points.append(bad_points)

print(*col_bad_tiles)
print(*col_bad_points)
print(total_tiles, total_points, f"{total_points * p:.2f}")
