import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for s,e,c in paths:
        # 양방향 그래프
        graph[s].append((e,c))
        graph[e].append((s,c))
    
    intensity = [1e9] * (n+1)  # 최소 intensity 저장
    
    q = []
    for gate in gates:
        heapq.heappush(q, (0, gate)) # 출입구는 모두 시작점 후보
        intensity[gate] = 0
    
    # 다익스트라
    while q:
        now_val, now_idx = heapq.heappop(q)
        if now_val > intensity[now_idx]:  # 이미 방문
            continue
        if now_idx in summits:  # 산봉우리
            continue
        for nxt_idx, nxt_val in graph[now_idx]:
            update = max(now_val, nxt_val)
            if update < intensity[nxt_idx]:
                intensity[nxt_idx] = update
                heapq.heappush(q, (update, nxt_idx))
    
    min_val = 1e9
    min_idx = 0
    for summit in sorted(summits):
        if intensity[summit] < min_val:
            min_val = intensity[summit]
            min_idx = summit
    
    return [min_idx, min_val]
