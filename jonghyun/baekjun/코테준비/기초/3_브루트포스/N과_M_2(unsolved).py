'''def factorial_1(n):
    if n <= 1 : # 손절라인
        return n # 달성하면 나가
    
    return n * factorial_1(n-1) # 달성할때가지 못나가
def factorial_2(n):
    if n > 1 : # 익절라인
        return n* factorial_2(n-1) # 달성할 때까지 못나가

    else :
        return n  #달성하면 나가
print(factorial_2(3))'''
'''
재귀 - 순열
n, m = map(int, input().split())

check = [0] * (n+1)
data = [0] * m

def DFS(L, n,m,start):
    if L == m :
        print(*data)
        return
    
    for i in range(start, n+1):
        if check[i]:
            # print(i)
            continue
        check[i] = True
        data[L] = i
        DFS(L+1, n, m, i+1)
        check[i] = False
DFS(0,n,m,1)  '''

# 재귀 - 선택
n, m = map(int, input().split())
data = [0]*m
def DFS(index, selected, n, m):
    if selected == m:
        print(*data)
        return
    if index > n:
        return
    data[selected] = index
    DFS(index+1, selected+1, n, m)
    data[selected] = 0
    DFS(index+1, selected, n, m)

DFS(1,0,n,m)