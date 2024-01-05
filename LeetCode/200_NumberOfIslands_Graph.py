class Solution:
    def numIslands(self, grid):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        row = len(grid)
        col = len(grid[0])
        res = 0

        def dfs(x, y):
            if x >= row or y >= col or x < 0 or y < 0 or grid[x][y] != '1':
                return
            grid[x][y] = '-'
            for i in range(4):
                dfs(x + dx[i], y + dy[i])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        return res
