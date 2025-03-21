n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range (n)]
check = [[False]*m for _ in range(n)]

count = 0
max_area = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def bfs(y,x):
    s = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range (4):
            rx = ex+dx[k]
            ry = ey+dy[k]
            if 0<=rx<m and 0<=ry<n:
                if map[ry][rx] == 1 and check[ry][rx] == False:
                    check[ry][rx] = True
                    s+=1
                    q.append((ry,rx))
    return s


for j in range (n):
    for i in range (m):
        if map[j][i] == 1 and check[j][i] == False:
            count+=1
            check[j][i] = True
            max_area = max(max_area, bfs(j,i))
print(count)
print(max_area)