n = int(input())
graph = [list(map(int,input().split())) for i in range(n)]


ans = -1
for i in range((1<<n)):
    first = []
    second = []
    for j in range(n):
        if (i&(1<<j)) > 0:
            first += [j]
        else :
            second += [j]
    if len(first) != n//2:
        continue
    t1 = 0
    t2 = 0
    for l1 in range(n//2):
        for l2 in range(n//2):
            if l1 == l2 :
                continue
            t1 += graph[first[l1]][first[l2]]
            t2 += graph[second[l1]][second[l2]]
    diff = abs(t1-t2)
    if ans == -1 or ans > diff:
        ans = diff

print(ans)
n = 4
for i in range((1<<n)):
    print(i)