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
    if x < m:   
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
    if 0<y:
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
    if y<m:
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
# print(data)