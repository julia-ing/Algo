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

# 양수는 내림차순 정렬해서 큰 수들부터 곱하기
pos.sort(reverse=True)
# 음수와 0은 작은 값들부터 곱하기
neg.sort()

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
