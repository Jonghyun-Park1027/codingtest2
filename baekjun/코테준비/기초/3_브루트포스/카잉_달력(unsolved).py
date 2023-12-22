
T = int(input())
# for _ in range(T):



'''ans = 1
m=1
n = 1
while True :
    if x == m and y == n:
        break
    if m == M and n == N:
        print(-1)
        break
    m , n = m +1, n+1
    if M < m    :
        # print(m)
        m = 1
    if N < n :
        n = 1
    ans += 1
if  m != M and n != N:
    print(ans)'''
for _ in range(T):
    M, N, x, y = map(int, input().split())
    x, y = x-1, y-1
    k = x
    while k < N*M:
        if k%N == y:
            print(k+1)
            break
        k += M
    else :
        print(-1)


