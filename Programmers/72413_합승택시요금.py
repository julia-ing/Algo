def solution(n, s, a, b, fares):
    d = [[10000000]*n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
        
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c
        
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]
    
    answer = 10000000
    for i in range(n):
        answer = min(answer, d[s-1][i] + d[i][a-1] + d[i][b-1])
    return answer
