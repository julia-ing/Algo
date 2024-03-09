from collections import defaultdict


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

subA = defaultdict(int)
subB = defaultdict(int)

for i in range(n):
    for j in range(i+1, n+1):
        subA[sum(A[i:j])] += 1

for i in range(m):
    for j in range(i+1, m+1):
        subB[sum(B[i:j])] += 1

res = 0
for a in subA:
    if T-a in subB:
        res += subA.get(a) * subB.get(T-a)

print(res)
