import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque([n])
dist = [0] * 10000001

while q:
    x = q.popleft()
    if x == k:
        print(dist[x])
        break
    for nx in (x*2, x-1, x+1):
        if not dist[nx] and 0<=nx<=len(dist):
            dist[nx] = dist[x] + 1
            q.append(nx)
