class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def dfs(x, y, flow):
            for i in range(4):
                nx = x + dx[i]  # 다음 데이터를 찾기 위해 x는 양옆으로 움직일 수 있음
                ny = y + dy[i]  # y는 위아래로 움직일 수 있음

                if nx < 0 or ny < 0 or nx >= m or ny >= n:  # 범위를 벗어나는 경우
                    continue
                if (nx, ny) not in flow:  # 인접한 데이터가 flow 에 없으면
                    if heights[nx][ny] >= heights[x][y]:  # nx,ny가 x,y 이상이어야 이전 데이터로 '흐를' 수 있음
                        flow.add((nx, ny))  # 데이터 추가
                        dfs(nx, ny, flow)  # 인접 데이터를 시작 데이터로 재귀 호출

        p = set()
        a = set()

        for i in range(m):
            p.add((i, 0))  # 왼쪽
            a.add((i, n-1))  # 오른쪽
            dfs(i, 0, p)  # pacific 데이터들을 각각 dfs의 시작으로 넣어줌
            dfs(i, n - 1, a)  # atlantic 데이터들을 각각 dfs의 시작으로 넣어줌

        for i in range(n):
            p.add((0, i))  # 위
            a.add((m-1, i))  # 아래
            dfs(0, i, p)
            dfs(m - 1, i, a)

        return list(p&a)  # 둘의 교집합을 반환
