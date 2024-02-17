import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e,c))

start, target = map(int, input().split())

INF = 1e9
distance = [INF] * (n+1)
paths = [""] * (n+1)

def dijkstra(s):
    q = []
    distance[s] = 0
    paths[s] = str(s)
    heapq.heappush(q, (0, s, str(s)))
    
    while q:
        dist, cur, path = heapq.heappop(q)
        if dist > distance[cur]:
            continue
        for nxt in graph[cur]:
            if dist + nxt[1] < distance[nxt[0]]:
                distance[nxt[0]] = dist + nxt[1]
                paths[nxt[0]] = path + " " + str(nxt[0])
                heapq.heappush(q, (dist + nxt[1], nxt[0], paths[nxt[0]]))
    return

dijkstra(start)
print(distance[target])
print(len(paths[target].split()))
print(paths[target])
