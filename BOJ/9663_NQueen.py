import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
    return True

def dfs(x):
    global res
    if x == N:
        res += 1
        return
    else:
        # x행의 각 열에 퀸을 놔보기
        for i in range(N):
            row[x] = i
            # 놓을 수 있으면 그 다음 행 체크
            if check(x):
                dfs(x+1)

N = int(input())
# 해당 행에 퀸이 있는 위치
row = [0] * N
res = 0
dfs(0)
print(res)
