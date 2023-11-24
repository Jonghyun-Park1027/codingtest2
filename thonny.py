n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]


s_t = []
l_t = []
check = [0]*(n)
answer = 10000
# i 행을 +1 하면서 구함
# j 열을 +1 하면서 구함
def go(L,s_t, l_t, check):
# L 이 n이 될떄 return
    global answer
    if L == n-1:
        answer = min(answer, sum(s_t)-sum(l_t))
        return
# if not n :
#     continue 또는 다른 방식으로 0 일때 캔슬해야함
    for i in range(n):
        if graph[L][i] == 0:
            continue
        if check[i] :
            continue
        if L == n/2 :
            l_t.append(graph[i][L])
            check[i] = True
            l_t.append(graph[L][i])
            check[L] = True
            go(L+1, s_t, l_t, check)
            l_t.pop()
            check[i] = False
            l_t.pop()
            check[L] = False
# i는 행, j는 열, 0은 자기자신
        else :
            s_t.append(graph[i][L])
            check[i] = True
            s_t.append(graph[L][i])
            check[L] = True
            go(L+1, s_t, l_t, check)
            s_t.pop()
            check[i] = False
            s_t.pop()
            check[L] = False

go(0, s_t, l_t, check)
print(answer)