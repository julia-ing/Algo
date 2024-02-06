N = int(input())
nums = list(map(int, input().split()))

certain = [0] * N

for i in range(N):
    # breakout 발견하면 그 숫자만큼 앞에는 확실함
    if nums[i] != -1:
        certain[i] = -1  # 이미 값이 있으므로 카운트에서 빼기
        certain[i- nums[i]] = 1  # 확실히 탈출함
        # 중간에 있는 값들은 확실히 탈출 안한 애들
        for j in range(i-nums[i]+1, i):
            # 근데 만약 탈출했다고 기록되었다면 모순이므로 -1 리턴
            if certain[j] == 1:
                print(-1)
                exit(0)
            certain[j] = -1

# 첫날은 확실
certain[0] = 1

certain_cnt, uncertain_cnt = 0, 0

for i in range(N):
    if certain[i] == 1:
        certain_cnt += 1
    elif certain[i] == 0:
        uncertain_cnt += 1

print(certain_cnt, certain_cnt + uncertain_cnt)
            