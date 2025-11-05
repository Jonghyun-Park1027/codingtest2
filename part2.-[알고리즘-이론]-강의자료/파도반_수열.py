g= [0] * 101

g[0] = g[1] = g[2] = 1
g[3] = g[4] = 2

for i in range(5, 101):
    g[i] = g[i-1] + g[i-5]

n = int(input())
for _ in range(n):
    t = int(input())

    print(g[t-1])