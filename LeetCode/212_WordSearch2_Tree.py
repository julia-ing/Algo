# time exceeded error...
class Solution:
    def search(self, word):
        self.used = set()

        def dfs(x, y, word):
            if (x >= self.m or x < 0) or (y >= self.n or y < 0) or (x, y) in self.used or word[0] != self.board[x][y]:
                return False

            if len(word) == 1:
                return True

            self.used.add((x, y))
            for i in range(4):
                nx = x + self.dx[i]
                ny = y + self.dy[i]
                if dfs(nx, ny, word[1:]):
                    return True
            else:
                self.used.remove((x, y))
                return False

        for r in range(self.m):
            for c in range(self.n):
                if dfs(r, c, word):
                    return True
        return False

    def findWords(self, board, words):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

        self.m = len(board)
        self.n = len(board[0])
        self.board = board

        res = []
        for word in words:
            if self.search(word):
                res.append(word)
        return res
