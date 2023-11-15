def DFS(L,n,k,data):
    if L == k:
        print(*data)
    else :
        for i in range(1, n+1):
            data.append(i)
            DFS(L+1, n, k, data)
            data.pop()
    # for i in range(1,n+1 ):
    # #     print(i)
    # if data[0] == n +1 :
    #     return
    # if len(data) != k -1:
    #     data.append(1)
    #     point += 1
    #     # print(data)
    #     print("point : ", point)
    #     DFS(n,k,point, data)
    # else :
    #     for i in range(1, n +1):
    #         print(*data, i)
    # else :
    #     print("data:",*data)
    #     data[start] += 1
    #     print("start:",start)

    #     if data[start] != n:
    #         print("data[start] : ", data[start])
    #         data[start] += 1
    #     else :
            
    #         data[start] = 1
    #         start -= 1
            
    #         DFS(n,k,start,data)
   
    
    
 
L = 0
n = 3
k = 2

data = []

DFS(L,n,k, data)