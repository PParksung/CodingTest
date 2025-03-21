from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input())) for _ in range (n)]
check = [[False]*m for _ in range (n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    q = deque()
    q.append((x,y))
    
    while q:
        x,y = q.popleft()
        for k in range (4):
            ry = y+dy[k]
            rx = x+dx[k]
            if ry < 0 or rx <0 or ry>=m or rx>=n:
                continue
            if graph[rx][ry]==0:
                continue
            if graph[rx][ry]==1:
                graph[rx][ry] = graph[x][y] + 1
                q.append((rx,ry))
    return graph[n-1][m-1]

print(bfs(0,0))
