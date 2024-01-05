from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
Q = deque()
Q.append([n])

visited = [False] * (n+1)

while Q:
    arr = Q.popleft()
    x = arr[0]
    if x == 1:
        answer = arr
        break
    if not visited[x]:
        visited[x] = True
        if x % 3 == 0:
            Q.append([x//3] + arr)
        if x % 2 == 0:
            Q.append([x//2] + arr)
        Q.append([x-1] + arr)

print(len(answer) - 1)
for i in range(len(answer)-1, -1, -1):
    print(arr[i], end = ' ')
