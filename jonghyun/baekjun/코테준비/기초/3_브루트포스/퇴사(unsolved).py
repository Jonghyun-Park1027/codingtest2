n = int(input())
data= []
day = [0]*n
pay = [0]*n
for i in range(n):
    day[i], pay[i] = map(int,input().split())
# print(n)
# pay 초기화
earn = 0
check = [0]* n
def DFS( index,cnt):
    global earn
    # print(index)

    # if index < n:
    if index == n :
        
        earn = max(earn, cnt)
        return
    if index > n:
        return
    # pay에 이전값을 저장하고 max 함수를 써서 최종값 산출

    # 리스트를 for문으로 순회하며 하나씩 대입 근데, index를 start로 계속 갱신해준다. index의 초기값은 0
    # for i in range(index, n):
    # index(n + data[0])가 n+1을 넘는다면 return
    

    # if index]:
        # continue
    
    # cnt += pay
    # index] = True
    # if index < n-1 :
        
    DFS( index+1, cnt)
    DFS( index+day[index], cnt+pay[index])
  

DFS(0,0)
print(earn) 