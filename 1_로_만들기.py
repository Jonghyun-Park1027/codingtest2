answer = 10000000

def calc(L, n,check):
    global answer
    # n 이 1이면 계산수 L을 리턴
    if L != 0 and n <= 1:
        answer = min(answer, L)
        return
    # for문을 통해 각자 모든 방법을 고려한다
    for i in range(3):
        if check[i] == 1:
            continue

        check[2] = 1
        calc(L+1, n-1, check)
        check[2] = 0       

        if n % 3 == 0 :

            check[0] = 1
            calc(L+1, n//3, check)
            check[0] = 0
        if n % 2 == 0:

            check[1] = 1
            calc(L+1, n//2, check)
            check[1] = 0

n = int(input())
check = [0]*3
calc(0, n, check)
print(answer)
# print(10//3)
# answer = 10000000
# def calc(L, n):
#     global answer
#     # n 이 1이면 계산수 L을 리턴
#     if L != 0 and n == 1:
#         answer = min(answer, L)
#         return
#     # n % 3 == 0 일 경우 나누고 함수 호출

#     if n % 3 == 0:
        
#         return calc(L+1, n//3)
#         # n *= 3
#     if n %2 == 0:
        
#         return calc(L+1, n//2)
#         n *= 2
    
#     return calc(L+1, n-1)
#     # return
#     # return L
# n = int(input())
# calc(0, n)
# print(answer)