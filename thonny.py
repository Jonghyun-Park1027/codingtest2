n, m = map(int,input().split())
check = [False] * (n + 1)
answer = [False] * m

data = []
def nm(start, n, m ):
    if start == m: # 손절라인
        return print(' '.join(map(str,answer))) # 달성했으면 돌아가
    
    for i in range(1,n+1):
        if check[i]:
            continue
        if i <= start :
            continue
        answer[start] = i
        check[i] = True
        
        nm(start+1,n,m)
        check[i] = False

nm(0,n,m)