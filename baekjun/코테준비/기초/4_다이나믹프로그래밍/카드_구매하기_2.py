from collections import defaultdict
# 카드팩데이터를 외부에서 구현
t = int(input())
# 갱신용 max 데이터
# answer = 0
# card = defaultdict(int)

graph = [0] + list(map(int,input().split()))
# d = [-1] * (n+1)
check = [-1] * (t+1)
check[0] = 0
for i in range(1, t+1):
    for j in range(1, i+1):
        if check[i] == -1 or check[i] > check[i-j] + graph[j]:
            check[i] = check[i-j] + graph[j]
print(check[t])