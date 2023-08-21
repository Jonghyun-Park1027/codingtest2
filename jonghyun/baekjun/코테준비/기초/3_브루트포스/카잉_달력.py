'''
unsolved : 구현실패
n = int(input())
for _ in range(n):
    count = 1
    M, N, x_t, y_t = map(int,input().split())
    x = 1
    y = 1
    while True:
        x += 1
        x %= M
        y += 1
        y %= N
        # if x % M == 0 :
            # y +=1
        count += 1
        if x_t == x and y_t == y :
            # print(f"count : {count}, x_t : {x_t}, x : {x}, y_t : {y_t}, y : {y}")
            print(count)
            break
        if M == x and N == y :
            print(-1)
            break
        # if M == x:
        #     x =0
        #     # print(x)
        # if N == y:
        #     y = 0'''
# 답
t = int(input())
for _ in range(t):
    m,n,x,y = map(int, input().split())
    x -=1
    y -=1
    k= x
    while k < n*m:
        if k % n == y:
            print(k+1)
            break
        k += m
    else :
        print(-1)