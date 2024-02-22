import heapq

# 1. 플로이드 워셜 풀이
V, E = map(int, input().split())
graph = [[1e9] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

res = 1e9
for i in range(1, V+1):
    res = min(res, graph[i][i])  # 사이클

if res == 1e9:
    print(-1)
else:
    print(res)



# 2. 다익스트라 풀이
graph = [[] for _ in range(V+1)]
dist = [[1e9] * (V+1) for _ in range(V+1)]

heap = []
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    dist[a][b] = c
    heapq.heappush(heap, [a, b, c])

flag = False
while heap:
    a, b, c = heapq.heappop(heap)
    
    # 사이클 완성
    if a == b:
        print(c)
        flag = True
        break
        
    # 저장된 거리보다 크면 넘어감
    if dist[a][b] < c:
        continue
    
    for nb, nc in graph[b]:
        new_dist = c + nc
        if new_dist < dist[a][nb]:
            dist[a][nb] = new_dist
            heapq.heappush(heap, [a, nb, new_dist])

if not flag:
    print(-1)
