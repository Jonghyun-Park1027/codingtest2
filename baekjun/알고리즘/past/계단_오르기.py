n = int(input())

t = [0] * 301
for i in range(1, n+1):
    t[i] = int(input())
g = [0] * 301

g[1] = t[1]
g[2] = t[1] + t[2]
g[3] = max(t[1] + t[3], t[2]+t[3])

for i in range(4, n + 1):
    g[i] = max(t[i] + t[i-1] + g[i-3], t[i]+ g[i-2])
print(g[n])