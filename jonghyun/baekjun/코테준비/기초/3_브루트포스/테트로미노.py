'''
unsolved : 아이디어 설정 실패, 시간초과로 인한 구현 실패
# 4개일떄 return
n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
def findmax(maxlen, currentlen, x,y, start):
    data = []
    # 좌로 이동
    if x >1:
        print("-x")
        currentlen +=1
        x -=1
        start += graph[y][x]
        if currentlen>4 :
            data.append(start)
            return data
        else :
            findmax(maxlen, currentlen, x,y, start)

    # 우로이동
    elif x < m:   
        print("+x")
        
        currentlen +=1
        x +=1
        start += graph[y][x]
        if currentlen>4 :
            data.append(start)
            return data
        else :
            findmax(maxlen, currentlen, x,y, start)

    # 위로이동
    elif 0<y:
        print("-y")
        
        currentlen +=1
        y -=1
        start += graph[y][x]
        if currentlen>4 :
            data.append(start)
            # print(start)
            return data
        else :
            findmax(maxlen, currentlen, x,y, start)

    # 아래로 이동
    elif y<m:
        print("+y")
        currentlen +=1
        y +=1
        start += graph[y][x]
        if currentlen>4 :
            data.append(start)
            return data
        else :
            findmax(maxlen, currentlen, x,y, start)
    return data

maxlen = 4
currentlen = 1
x = 0
y = 0
start = graph[y][x]
print(findmax(maxlen, currentlen, x,y, start))
# print(data)'''

# 답
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
ans =0
for i in range(n):
    for j in range(m):
        for block in blocks:
            ok = True
            s = a[i][j]
            for dx, dy in block:
                x, y = i+dx, j +dy
                if 0 <= x <n and 0 <=y < m:
                    s += a[x][y]
                else :
                    ok =False
                    break
            if ok and ans < s:
                ans = s
print(ans)