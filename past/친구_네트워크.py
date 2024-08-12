import sys
input = sys.stdin.readline
def find(x):
    if x == g[x]:
        return x
    else :
        g[x] = find(g[x])
        return g[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        g[y] = x
        number[x] += number[y]

t = int(input())
for _ in range(t):
    f = int(input())
    g = dict()
    number = dict()
    for _ in range(f):
        x, y = input().split()

        if x not in g:
            g[x] = x
            number[x] = 1
        if y not in g:
            g[y] = y
            number[y] = 1
        union(x,y)
        print(number[find(x)])
