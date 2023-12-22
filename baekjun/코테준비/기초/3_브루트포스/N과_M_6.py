n,m = map(int,input().split())
data = sorted(map(int, input().split()))
start = 0
check = [0]* 10001
answer = []

def DFS(L, data, m, start, check,answer):
    if L == m :
        print(*answer)
        return
    for i in range(start, len(data)):
        if check[data[i]]:
            continue
        check[data[i]]= True
        answer.append(data[i])
        DFS(L+1, data, m, i+1, check, answer)
        answer.pop()
        check[data[i]] = False

DFS(0, data, m, start, check, answer)

