import sys
input = sys.stdin.readline
# 동생의 수 n, 수빈이의 현재위치 s
n ,s = map(int,input().split())

# 전체 동생 위치
g = list(map(lambda x: abs(x-s), list(map(int,input().split()))))

answer = 100000000000

t = max(g)

# gcd 만들기
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)

# t와 
for i in g :
    answer = min(answer, GCD(t, i))
print(answer)