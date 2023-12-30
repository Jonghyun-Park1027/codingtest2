# 팩토리얼 함수 만들기

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
n = int(input())
t = str(factorial(n))
# print(t)
answer = 0
for i in range(len(t)-1, -1, -1):
    if t[i] == '0':
        answer += 1
        
        
    else :
        print(answer)
        break




# print(t[-1])