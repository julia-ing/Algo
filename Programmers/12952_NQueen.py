def solution(n):
    col = [0]*n
    def check(x, y, col):
        for i in range(x):
            if col[i] == y or abs(y - col[i]) == x - i:
                return False
        return True

    def queen(x, col):
        if x == n:
            return 1
        cnt = 0
        for y in range(n):
            if check(x, y, col):
                col[x] = y
                cnt += queen(x + 1, col)

        return cnt
    return queen(0, col)
