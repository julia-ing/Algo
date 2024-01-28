a, b, x, y = map(int, input().split())

# teleportation 사용 x
default = abs(b - a)
# teleportation
teleportation = min(abs(a-x), abs(a-y)) + min(abs(b-x), abs(b-y))

res = min(default, teleportation)
print(res)