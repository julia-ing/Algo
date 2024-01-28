from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

def bfs(usado, start, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    res = 0
    while q:
        curr = q.popleft()
        for n, u in graph[curr]:
            if not visited[n] and u >= usado:
                res += 1
                q.append(n)
                visited[n] = 1
    return res

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for _ in range(Q):
    k, v = map(int, input().split())
    visited = [0] * (N+1)
    res = bfs(k, v, visited)
    print(res)
