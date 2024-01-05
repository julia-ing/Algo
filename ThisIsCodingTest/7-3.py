n, m = map(int,input().split())

lens = list(map(int, input().split()))

start = 0
end = max(lens)

res = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for l in lens:
        if l > mid:
            total += (l - mid)
    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)
