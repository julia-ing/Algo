N = int(input())

nums = [int(input()) for _ in range(N)]

res = 0
pos = []
neg = []
for n in nums:
    if n == 1:
        res += 1
    elif n > 1:
        pos.append(n)
    elif n <= 0:
        neg.append(n)
        
pos.sort(reverse=True)
neg.sort()

# 양수면 곱하는게 이득
while pos:
    if len(pos) == 1:
        res += pos.pop(0)
    else:
        res += pos.pop(0) * pos.pop(0)

while neg:
    if len(neg) == 1:
        res += neg.pop(0)
    else:
        res += neg.pop(0) * neg.pop(0)

print(res)
