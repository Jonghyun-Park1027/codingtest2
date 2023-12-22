# # answer = 10000000
# import sys
# def calc(n):
#     global answer
#     # n 이 1이면 계산수 L을 리턴
#     if n <= 1:
#         return 0
#     # for문을 통해 각자 모든 방법을 고려한다
#     if check[n] > 0 :
#         return check[n]
#     check[n] = calc(n-1) + 1
#     if n %2 == 0:
#         temp = calc(n//2) + 1
#         if check[n] > temp :
#             check[n]= temp
#     if n % 3 == 0 :
#         temp = calc(n//3) + 1
#         if check[n] > temp:
#             check[n] = temp
#     return check[n]

# n = int(sys.stdin.readline())
# check = [0]*(n+1)
# print(calc(n))

n = int(input())
d= [0] * (n+1)
d[1] = 0
for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i%2 == 0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2] + 1
    if i%3 == 0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3] + 1
print(d[n])