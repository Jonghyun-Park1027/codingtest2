e, s, m = map(int, input().split())

ans = 1
while True:
    if e == s == m == 1 :
        break
    ans += 1
    e, s, m = e-1, s-1, m-1
    if e == 0:
        e = 15
    if s == 0:
        s = 28
    if m == 0 :
        m = 19
print(ans)