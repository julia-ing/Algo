from collections import deque, defaultdict

def solution(edges):
    graph = defaultdict(list)
    indir = defaultdict(int)
    outdir = defaultdict(int)
    nodes = set()
    
    for s, e in edges:
        graph[s].append(e)
        indir[e] += 1
        outdir[s] += 1
        nodes.add(s)
        nodes.add(e)
    
    # 생성 정점
    start = 0
    for node in nodes:
        if indir[node] == 0 and outdir[node] >= 2:
            start = node
            break
    
    # 생성 정점 관련 정보들 제거
    nodes.remove(start)
    for node in graph[start]:
        indir[node] -= 1
    
    # visited 표시를 위한 bfs
    visited = {node: False for node in nodes}
    def bfs(x):
        q = deque([x])
        visited[x] = True
        while q:
            node = q.popleft()
            for nnode in graph[node]:
                if not visited[nnode]:
                    visited[nnode] = True
                    q.append(nnode)
    # 모양 분류
    donut, stick, eight = 0, 0, 0
    for node in nodes:
        if visited[node]:
            continue
        # 막대: 들어오는 간선은 없고 나가는 간선은 0개 이상
        if indir[node] == 0 and outdir[node] >= 0:
            bfs(node)
            stick += 1
            continue
        # 8자는 2개씩 들어오고 나가는 간선이 존재함
        if indir[node] == 2 and outdir[node] == 2:
            bfs(node)
            eight += 1
            continue
    # 막대, 8자 분류 후 남아있는 모양은 도넛
    for node in nodes:
        if visited[node]:
            continue
        bfs(node)
        donut += 1
    
    return [start, donut, stick, eight]