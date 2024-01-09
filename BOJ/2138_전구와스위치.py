N = int(input())
prev = list(map(int, input().rstrip()))
goal = list(map(int, input().rstrip()))

def turn(prev):
    num = 0
    # 처음과 마지막 사이에 있는 전구들은 3개씩 전환
    for i in range(1, N-1):
        if prev[i-1] != goal[i-1]:
            prev[i-1] = int(not prev[i-1])
            prev[i] = int(not prev[i])
            prev[i+1] = int(not prev[i+1])
            num += 1
    # 마지막 전구
    if prev[N-1] != goal[N-1]:
        prev[N-2] = int(not prev[N-2])
        prev[N-1] = int(not prev[N-1])
        num += 1
    if prev == goal:
        return num
    else:
        return 1e9

# 첫번째 전구를 키는 경우
prev1 = prev.copy()
prev1[0] = int(not prev[0])
prev1[1] = int(not prev[1])
res1 = turn(prev1)

# 첫번째를 안켜는 경우
prev2 = prev.copy()
res2 = turn(prev2)

ans = min(res1+1, res2)
# 불가능한 경우 -1 리턴
if ans == 1e9:
    print(-1)
else:
    print(ans)