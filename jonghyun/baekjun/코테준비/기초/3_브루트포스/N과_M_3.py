'''def fact_1(n):
    if n > 1: # 익절라인
        return n*fact_1(n-1)  # 달성할 때까지 못나가
    
    return n# 특정값, 일정값 ,입력값

def fact_2(n):
    if n <=1: # 손절라인
        return n 
    # else: 생략가능
    return n*fact_2(n-1) # 달성할때까지 못나가

print(fact_2(3))'''



n, m = map(int,input().split())

check = [0]* (n +1)
answer = [0]* m

def nm(start,n,m):
    if m == start:
        return print(" ".join(map(str,answer)))
    
    for i in range(1, n+1):
        # if check[i] :
        #     continue

        # check[i] = True
        answer[start] = i
        nm(start+1, n, m)
        # check[i]= False

nm(0, n, m)