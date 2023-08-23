'''def fact_1(n):
    if n <= 1 : # 손절라인
        return n
    
    else :
        return n* fact_1(n-1)
    
def fact_2(n):
    if n > 1 :# 익절라인
        return n * fact_2(n-1)
    
    return n

print(fact_2(3))'''


n, m = map(int, input().split())

answer = [0]* m
check = [0] * (n+1)

def nm(start,index, n, m):
    if start == m:
        return print(" ".join(map(str,answer)))
    for i in range(index, n+1):

        answer[start]=i
        nm(start+1,i,n,m)


nm(0,1,n,m)