fn, f = map(int,input().split())
c = int(input())
n = int(input())
if (fn*n) + f <= c*n and fn <= c:
    print(1)
else :
    print(0)