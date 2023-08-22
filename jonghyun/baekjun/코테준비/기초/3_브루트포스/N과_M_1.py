n, m = map(int,input().split())
c = [False] * (n+1)
a = [False]*m

def array(start, n, m):
    if start== m:# 손절라인

        return print(' '.join(map(str,a)))# 달성하면 돌아가
    for i in range(1,n+1):
        if c[i]:
            continue
        c[i] = True
        a[start] = i
        # data = [start]
        # if j != data[0]:
        array(start+1,n,m)# 달성할때까지 못나가
        c[i]=False
        
        
'''def array():
    if : #달성할때까지 못나가
        return # 재귀문
    else :
        return #입력값 특정값 일정값'''
array(0,n,m)





'''def factorial_1(n):
    if n <= 1: # 손절라인
        return n#달성하면 돌아가
    
    return n * factorial_1(n-1)# 달성할 때까지 못나가

def factorial_2(n):
    if n > 1: # 익절라인
        return n * factorial_2(n-1) #달성할 때까지 못나가
    else :
        return n # 달성하면 돌아가
print(factorial_1(3))'''
    