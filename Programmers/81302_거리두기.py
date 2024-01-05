dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, place, visited, step):
    if step == 2:
        return True
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and place[nx][ny] != 'X':
            if place[nx][ny] == 'P':
                return False
            else:
                if dfs(nx,ny,place,visited,step+1) == False:
                    return False

def search(place, visited):
    for i in range(5):	
        for j in range(5):
            if place[i][j] == 'P' and not visited[i][j]:
                if dfs(i,j,place,visited,0) == False:
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        visited = [[False]*5 for _ in range(5)]
        if search(place,visited):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer
