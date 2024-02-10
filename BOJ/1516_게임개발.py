from collections import deque

N = int(input())
time = [0] * (N+1)
# 위상정렬을 위한 그래프
graph = [[]*(N+1) for _ in range(N+1)]
indegree = [0] * (N+1)
dp = [0] * (N+1)

for i in range(1, N+1):
    info = list(map(int, input().split(" -1")[0].split()))
    time[i] = info[0]
    for n in info[1:]:
        graph[n].append(i)
        indegree[i] += 1

def topology():
    q = deque()
    # 진입차수가 0인 애들을 찾아 큐에 넣기
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    
    while q:
        v = q.popleft()
        for nv in graph[v]:
            # 방문: 진입차수 빼주고 dp 배열 업데이트
            indegree[nv] -= 1
            dp[nv] = max(dp[nv], dp[v] + time[nv])
            # 진입차수가 0이 되어 시작점이 되었다면 append
            if indegree[nv] == 0:
                q.append(nv)

topology()
for i in range(1, N+1): 
    print(dp[i])
