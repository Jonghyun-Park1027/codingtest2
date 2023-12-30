import sys
input = sys.stdin.readline

n = int(input())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
for _ in range(n):
    a, b= map(int,input().split())
    g = gcd(a,b)
    print(int(g*((a/g)*(b/g))))