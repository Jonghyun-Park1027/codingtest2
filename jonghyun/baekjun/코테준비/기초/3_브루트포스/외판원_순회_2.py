def go(data):
    i = len(data) -1
    # data[i] >= data[i-1]인 경우를 유지하여 -1까지 서치
    while i > 0 and data[i-1] >= data[i]:
        i -=1

    if i <= 0 :
        return False
    
    j = len(data) - 1
    while data[j] < data[i-1] :
        j -= 1
    
    data[j], data[i-1] = data[i-1], data[j]

    j = len(data) - 1
    while i < j :
        data[i], data[j] = data[j], data[i]
        j -= 1
        i += 1
    return True

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
data = [i for i in range(n)]
# check = [0] * n
# graph[L][i]를 통한 행별로 조회
answer = 2147483647
def calc(data):
    # print(data)
    cnt = 0
    for i in range(1, n):        
        if graph[data[i-1]][data[i]] == 0 :
            continue
        cnt += graph[data[i-1]][data[i]]
    cnt += graph[data[-1]][data[0]]
    return cnt
# print(graph)

while True:
  
    temp = calc(data)
    answer = min(answer, temp)
#   print(answer)
    if not go(data):
        break
print(answer)
