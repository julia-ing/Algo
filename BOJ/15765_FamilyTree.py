# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

def find_relationship(a, b, parent, depth):
    try:
        common = lca(a, b)  # 최소 공통 조상
        atoc = depth[a] - depth[common]
        btoc = depth[b] - depth[common]

        # 최소 조상까지 거리가 하나 하나 -> siblings
        if atoc == 1 and btoc == 1:
            return "SIBLINGS"
        # 최소 조상까지 거리가 2 이상, 1 -> aunt
        elif (atoc > 1 and btoc == 1) or (atoc == 1 and btoc > 1):
            depth_diff = max(atoc, btoc)
            if atoc == 1:
                up = a
                down = b
            else:
                up = b
                down = a
            relation = "great-" * (depth_diff - 2) + "aunt"
            return f"{up} is the {relation} of {down}"
        # 최소 조상까지 0인 게 존재 -> mother
        elif atoc == 0 or btoc == 0:
            depth_diff = max(atoc, btoc)
            if atoc == 0:
                up = a
                down = b
            else:
                up = b
                down = a
            if depth_diff == 1:
                return f"{up} is the mother of {down}"
            relation = "great-" * (depth_diff - 2) + "grand-mother"
            return f"{up} is the {relation} of {down}"
        else:
            return "COUSINS"
            
    # 최소 공통 조상을 못찾는 경우    
    except:
        return "NOT RELATED"


n, a, b = input().split()
n = int(n)
parent = {}  # 각 사람의 부모를 저장
depth = {}  # 각 사람의 깊이를 저장
ppl = set() # 모든 사람

# 가계도 정보 입력 받기
for _ in range(n):
    p, c = input().split()
    parent[c] = p
    ppl.add(p)
    ppl.add(c)

# 각 사람의 깊이 계산하기
for target in ppl:
    depth[target] = 0
    cur = target
    while cur in parent:
        cur = parent[cur]
        depth[target] += 1

# 두 사람의 관계 찾기
relation = find_relationship(a, b, parent, depth)
print(relation)
