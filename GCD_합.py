# gcd 최대공약수 구하는 함수부터 만든다

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a%b)

def calc(L, g):
    if len(g) == 2 :
        a, b = g
        answer.append(gcd(a,b))
        return 
    for i in range(L,t_n):

        g.append(t[i])
        calc(i+1, g)
        g.pop()

n = int(input())
answer = []
for _ in range(n):
    t = list(map(int,input().split()))    
    t_n, t = t[0], t[1:]
    calc(0, [])
    print(sum(answer))
    answer = []