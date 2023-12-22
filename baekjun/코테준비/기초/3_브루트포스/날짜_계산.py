E, S, M = map(int,input().split())

ans = 1
while True :
    if E == S == M == 1:
        # print(1)
        break
    # E
    E -=1
    if E == 0 :
        E = 15
    # S
    S -=1
    if S == 0:
        S = 28
    # M
    M -=1
    if M == 0 :
        M = 19
    ans += 1

print(ans)