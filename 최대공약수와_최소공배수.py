a, b = map(int,input().split())

# gcd 최대 공약수 구하기

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
g = gcd(a,b)
print(g)

l = g * (a/g) * (b/g)
print(int(l))