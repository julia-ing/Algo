# 정답 참고
N = int(input())

if N <= 2:
    print(1)
else:
    cows = list(map(int, input().split()))
    cows.sort()

    receive_cnt = [0] * N # 패스 받은 수
    next_dir = [''] * N # 패스 넘길 위치
    for i in range(N):
        if i == 0: # 0번 위치 소는 오른쪽으로만 넘긴다
            receive_cnt[1] += 1
            next_dir[0] = 'R'
        elif i == N-1: # 마지막 소는 왼쪽으로만 넘긴다
            receive_cnt[N-2] += 1
            next_dir[N-1] = 'L'
        else: # 중간에 있는 소들은 양 옆 비교, 같으면 왼쪽으로
            if cows[i+1] - cows[i] < cows[i] - cows[i-1]:
                receive_cnt[i+1] += 1
                next_dir[i] = 'R'
            else:
                receive_cnt[i-1] += 1
                next_dir[i] = 'L'

    balls = 0
    for i in range(N):
        # 공을 못받은 소들
        if receive_cnt[i] == 0:
            balls += 1
        # 공을 서로에게만 주고받는 소들
        if receive_cnt[i] == 1 and (i < N-1 and receive_cnt[i+1] == 1) and next_dir[i] == 'R' and next_dir[i+1] == 'L':
            balls += 1

    print(balls) 
