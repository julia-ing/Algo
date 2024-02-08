n, m, k = map(int, input().split())
hierarchy = list(map(int, input().split()))
order = [list(map(int, input().split())) for _ in range(k)]

positions = {}  # 각 순서에 있는 소

for cow, pos in order:
    positions[pos] = cow

for i in range(1, n + 1):
    # 이미 위치가 정해져 있다면 넘어감
    if i in positions:
        continue

    temp_pos = positions.copy()
    
    # 1을 한번씩 넣어봄
    temp_pos[i] = 1
    
    flag = True
    cur_pos = 1
    for cow in hierarchy:
        # 위치가 정해져있는 소
        if cow in temp_pos.values():
            # 현재 위치보다 정해진 위치가 빠르면 잘못된 순서임
            # 3 1 5 4 0 0
            if cur_pos > list(temp_pos.keys())[list(temp_pos.values()).index(cow)]:
                flag = False
                break
            cur_pos = list(temp_pos.keys())[list(temp_pos.values()).index(cow)] + 1
        # 위치가 안정해져있는 소
        else:
            # 점유되지 않은 위치 찾기
            while cur_pos in temp_pos:
                cur_pos += 1
            temp_pos[cur_pos] = cow
    
    if flag:
        print(i)
        break
