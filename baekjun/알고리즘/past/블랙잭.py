import sys
n, m = map(int, input().split())
g = list(map(int, input().split()))
ans = 0
check = [False] * n
for i in range(n) :
    check[i] = True
    for j in range(n):
        if check[j] :
            continue
        check[j] = True
        for k in range(n):
            # print(k)
            if check[k] :
                continue
            t = g[i] + g[j] + g[k]
            # print(k)

            if t > m :
                continue
            # print(t)
            elif t == m:
                print(t)
                sys.exit()
            else:
                ans = max(ans, t)
        check[j] = False
    check[i] = False
print(ans)
# print(check)