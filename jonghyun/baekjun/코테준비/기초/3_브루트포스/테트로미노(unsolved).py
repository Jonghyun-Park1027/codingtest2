'''# direction : 1이 가로 0이 세로
def block_1(graph, x,y, n, m, direction):
    if x+4 > n or y+4 > m :
        return 0
    elif direction == 1: # 가로
        ans = 0
        for i in range(4):
            ans += graph[y+i][x]
        return ans
    elif direction == 0:
        ans = 0
        for i in range(4): # 세로
            ans += graph[x][y+i]
        return ans
    
n, m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# print(graph)
ans = 0
for x in range(n):
    for y in range(m): # 가로찾기
        result = block_1(graph, x, y, n, m, 1)
        if ans < result :
            ans = result
    for y in range(m): # 세로찾기
        result = block_1(graph, x, y, n, m, 0)
        if ans < result :
            ans = result
print(ans)'''
blocks = (
    ("1111"),
    ("11",
     "11"),
    ("10",
     "10",
     "11"),
    ("10",
     "11",
     "01"),
    ("111",
     "010")
)
blocks = (
    ((0,1), (0,2), (0,3)),
    ((1,0), (2,0), (3,0)),
    ((1,0), (1,1), (1,2)),
    ((0,1), (1,0), (2,0)),
    ((0,1), (0,2), (1,2)),
    ((1,0), (2,0), (2,-1)),
    ((0,1), (0,2), (-1,2)),
    ((1,0), (2,0), (2,1)),
    ((0,1), (0,2), (1,0)),
    ((0,1), (1,1), (2,1)),
    ((0,1), (1,0), (1,1)),
    ((0,1), (-1,1), (-1,2)),
    ((1,0), (1,1), (2,1)),
    ((0,1), (1,1), (1,2)),
    ((1,0), (1,-1), (2,-1)),
    ((0,1), (0,2), (-1,1)),
    ((0,1), (0,2), (1,1)),
    ((1,0), (2,0), (1,1)),
    ((1,0), (2,0), (1,-1)),
)
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            ok = True
            s = a[i][j]
            for dx, dy in block:
                x, y = i+dx, j+dy
                if 0 <= x < n and 0 <= y < m:
                    s += a[x][y]
                else:
                    ok = False
                    break
            if ok and ans < s:
                ans = s
print(ans)