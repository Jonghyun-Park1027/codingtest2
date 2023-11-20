# 테스트 케이스
T = int(input())
# n = int(input())
n=4
# 1,2,3 리스트 초기화
data = [1,2,3]
# check 배열 초기화(for문에 넣어야함)
check = [0] * n
# answer 초기화 (for문에 넣어야함)
answer = 0
cnt = 0
# DFS 함수 선언(n, check)
def DFS(n, cnt,answer):
# n 이 되었을때 cnt += 1 
    if n == cnt:
        answer += 1
        return
# 하나씩 넣고 다음 리스트를 찾는다 if continue
    for i in data:
        cnt += i
        DFS(n, cnt,answer)
        cnt -= i

# 그후 종료되면 answer를 출력
    print(answer)
DFS(n, cnt,answer)