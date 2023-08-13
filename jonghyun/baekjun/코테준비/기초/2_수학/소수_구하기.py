'''
unsolved : 제한시간 초과 및 구현실패
MAX = 1000001
d = [[1] for i in range(MAX+1)]
answer = []
n, m = map(int,input().split())
for i in range(2,MAX):
    for j in range(n, m+1):
        if j% i == 0:
            count =1
            while count * i < MAX:
                d[count * i] = 0
                count +=1
for i in range(2,m+1):
    count =1
    while count * i < MAX:
        d[count * i] = 0
        count +=1
    # 방문처리 완료
for i in range(MAX) :
    if d[i] == 1:
        print(i)
    if i == m:
        break
print(d[:17])
    # if d[i] != 0 :
    #     count =1
    #     while count * i > MAX:
    #         d[count * i] = 0
    #         count += 1
        
'''
MAX = 1000000
check = [0]*(MAX+1)
check[0] = check[1]= True

for i in range(2, MAX+1):
    if not check[i]: # not 0 == True
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i
m, n =map(int,input().split())
for i in range(m, n+1):
    if check[i] == False : # check[i]== 0일 경우
        print(i)
