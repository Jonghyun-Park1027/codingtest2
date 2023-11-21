n = int(input())
data= []
for _ in range(n):
    data.append(list(map(int,input().split())))

# pay 초기화
earn = 0
check = [0]* n
def DFS(check, index,cnt):
    global earn
    # print(index)
    if index > n-1:
        return
    if index < n:
        if earn < cnt :
            
            earn = max(earn, cnt)
        return

    # pay에 이전값을 저장하고 max 함수를 써서 최종값 산출

    # 리스트를 for문으로 순회하며 하나씩 대입 근데, index를 start로 계속 갱신해준다. index의 초기값은 0
    for i in range(index, n):
    # index(n + data[0])가 n+1을 넘는다면 return
        day, pay = data[i]  
        if check[index]:
            continue

        cnt += pay
        check[index] = True
        DFS(check, index+day, cnt)
        check[index] = False
        cnt -= pay

DFS(check, 0, 0)
print(earn) 