#아이디어
#2중 for문. 값1 && 방문X -> BFS
#BFS돌면서 그림 개수 +1, 최대값 갱신

#시간복잡도
#BFS(V+E)
#V : m*n
#E : V*4
#m,n 최대 500이니까
#V:500*500
#E : 4*500*500
#V+E = 5*250000

#자료구조
#그래프 전체 지도 : int[][]
#방문 : bool[][]
#Queue(BFS)

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range (n)]
check = [[False]*m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y,x):
    rs = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and check[ny][nx] == False:
                    rs +=1
                    check[ny][nx] = True
                    q.append((ny,nx))
    return rs

count = 0
maxv = 0

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and check[j][i] == False:
            check[j][i] = True
            #전체그림갯수 +1
            count += 1
            #BFS-> 그림크기 구해주고
            maxv = max(maxv, bfs(j,i))
            #최대값 갱신

print(count)
print(maxv)

