def DFS(n,k, start, data):

    if len(data) == k :
        print(*data)
        data[start] += 1
        print(start)
        if start == -1 :
            return  
        if data[start] == n:
            data[start] = 1
            start -= 1
            data[start] += 1

    data.append(1)
    start += 1
    print(data)
    DFS(n,k,start, data)
    
n = 3
k = 2
start = -1
data = []

DFS(n,k,start, data)