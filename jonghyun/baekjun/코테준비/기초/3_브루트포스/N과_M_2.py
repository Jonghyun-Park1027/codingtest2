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

n, m = map(int,input().split())
check = [False] * (n + 1)
answer = [False] * m

data = []
def nm(start,num, n, m ):
    if start == m: # 손절라인
        return print(' '.join(map(str,answer))) # 달성했으면 돌아가
    
    for i in range(num,n+1):
        if check[i]:
            continue
        # if i <= start:
            # continue
        answer[start] = i
        check[i] = True
        
        nm(start+1,i+1,n,m)
        check[i] = False

nm(0,1,n,m)