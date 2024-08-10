from collections import deque
import sys
t= int(input())
for _ in range(t):

    n, m = map(int,input().split())
    g = deque(list(map(int, input().split())))
    # print("?")

    g_idx = deque([False for i in range(n)])
    g_idx[m] = True
    # print("g :",g)
    # print("g_idx :", g_idx)
    # 첫번째 문서의 중요도를 확인
    ans = 1
    while True :
        # cnt를 g의 가장 큰 중요도로 초기화하며 cnt와 같을경우 출력 아닐경우 g와 g_idx를 -1 회전
        cnt = max(g)
        # print("cnt: ",cnt)
        if g[0] == cnt :
            if g_idx[0] :
                print(ans)
                break
            else :
                g.popleft()
                g_idx.popleft()
                ans += 1
        else :
            g.rotate(-1)
            g_idx.rotate(-1)

        

# g.rotate(-1)

