from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

# 정점, 루트, 쿼리
N, R, Q = map(int, input().split())
graph = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
dp = [1] * (N+1)

def dfs(now):
    visited[now] = 1
    
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs(nxt)
            dp[now] += dp[nxt]

dfs(R)

for i in range(Q):
    q = int(input())
    print(dp[q])