# 테스트 케이스
T = int(input())

# 1,2,3 리스트 초기화
data = [1,2,3]


# DFS 함수 선언(n, check)
def DFS(n, cnt, start):
    # answer를 global에 쓴다
    global answer
# n 이 되었을때 cnt += 1 
    if n == cnt:
        # print("activate")
        answer += 1
        # print(answer)
        return 
# 하나씩 넣고 다음 리스트를 찾는다 if continue
    for i in range(start, 3):
        # if start[i] == True :
        #     continue
        if cnt + data[i] > n :
            # cnt -=data[i]
            continue
        # start[i] = True
        cnt += data[i]
        DFS(n, cnt, start)
        cnt -= data[i]
    # start += 1

# for문을 돌며 n 할당
for i in range(T):
    # answer 초기화 (for문에 넣어야함)
    answer = 0
    cnt = 0
    n = int(input())
    # start 만들기
    check = [0] * n
    start =0
    DFS(n, cnt, start)
# 그후 종료되면 answer를 출력
    print(answer)