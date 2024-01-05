origin = input()
row = int(origin[1])
col = int(ord(origin[0]) - 97) + 1

direction = [[-2, -1], [2, 1], [1, 2], [-1, -2], [2, -1], [-1, 2], [-2, 1], [1, -2]]
res = 0

for d in direction:
    nrow = row + d[0]
    ncol = col + d[1]
    if nrow >= 1 and ncol >= 1 and nrow <= 8 and ncol <= 8:
        res += 1

print(res)
