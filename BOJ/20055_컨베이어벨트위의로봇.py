N, K = map(int, input().split())
belt = list(map(int, input().split()))

# 리스트 회전
def rotate(arr):
    arr.insert(0, arr.pop(-1))
    return arr

robot = [0] * N  # 로봇 여부
res = 0  # 단계

while True:
    res += 1
    # 1. 벨트가 각 칸 위 로봇과 함께 한 칸 회전
    belt = rotate(belt)
    robot = rotate(robot)
    
    if robot[N-1]:  # 회전 후 로봇이 내리는 위치에 있으면 내리기
        robot[N-1] = 0
    
    # 2. 가장 먼저 올라간 로봇부터 이동 가능하면 이동
    for i in range(N-2, -1, -1):
        # 로봇이 있는 칸들에 대해, 다음 칸에 로봇이 없고 내구도가 1 이상
        if robot[i] and not robot[i+1] and belt[i+1] >= 1:
            belt[i+1] -= 1
            robot[i+1] = 1
            robot[i] = 0

    if robot[N-1]:  # 이동 후 로봇이 내리는 위치에 있으면 내리기
        robot[N-1] = 0
    
    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
    
    # 4. 내구도가 0인 칸의 개수가 K개 이상이면 종료
    if belt.count(0) >= K:
        break

print(res)
