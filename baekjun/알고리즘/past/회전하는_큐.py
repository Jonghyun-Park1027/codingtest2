from collections import deque
n, m = map(int,input().split())
q = deque([i for i in range(1, n+1)])
t = list(map(int,input().split()))


answer = []
# 첫번째 원소 뽑기

# t 순회
for i in t:
# 왼쪽으로 한칸 
    # q 초기화
    q = deque([i for i in range(1, n+1)])
    # 정답후보 초기화   
    num = 0
    while True :
        if i == q[0] :
            answer.append(num)
            break
        
        q.popleft()
        q.rotate(-1)
        num += 1
# 오른쪽으로 한칸


print(answer)


