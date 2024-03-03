from collections import defaultdict

N = int(input())
graph = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[b].append(a)

def dfs(v):
    visited[v] = 1
    for n in graph[v]:
        if not visited[n]:
            dfs(n)

res = -1
for i in range(1, N+1):
    visited = [0]*(N+1)
    dfs(i)
    # 모든 정점에서 도달 가능하면 출력
    if all(visited[1:]):
        res = i
        break

print(res)

