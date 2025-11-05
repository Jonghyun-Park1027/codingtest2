N = int(input())
answer = 0
cnt = -1
for _ in range(N):
    temp = list(map(int, input().split()))
    # print(temp)
    minimum = min(temp)
    temp_cnt = temp.index(minimum)

    print(cnt)
