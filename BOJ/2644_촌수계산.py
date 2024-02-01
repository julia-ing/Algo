n = int(input())
a, b = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

def dfs(x):
    for v in relation[x]:
        if not num_visited[v]:
            num_visited[v] = num_visited[x] + 1
            dfs(v)

num_visited = [0] * (n+1)
dfs(a)

if num_visited[b] == 0:
    print(-1)
else:
    print(num_visited[b])
