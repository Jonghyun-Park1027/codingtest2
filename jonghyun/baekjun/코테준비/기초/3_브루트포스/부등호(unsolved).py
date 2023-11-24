
def ok(x, y, op):
    if op == '<':
        if x >y:
            return False
    if op == '>':
        if x < y:
            return False
    return True
def go(L, cnt):
    # global data
    # 체크배열에 따라서 계속 추가해주고 길이가 충족이 안되면 return하는 내용
    # if len(cnt) != n:
    #     return
    # 한개 완성할 경우 cnt data에 넣고 초기화
    if L == n+1:
        
        data.append(cnt)
        # print(cnt)
        # cnt = []
        return
    # n크기만큼 for문 돈다
    for i in range(10):
        # check가 1일경우 continue
        if check[i]:
            continue        
        # # L로 부등호를 조회해서 조건을 나눠준다.
        # if ineq[L] == 0: # 0 즉, 현재가 다음꺼보다 클때 ('>')
        #     if i < i+1 :
        #         print('>')
        #         continue
        # if ineq[L] == 1: # 1 즉, 현재가 다음꺼보다 작을 때('<')
        #     if i > i+1 :
        #         print('<')
        #         continue
        # cnt에 i를 추가하고 check[i]을 True로 변경
        # cnt.append(i+1)
        if L == 0 or ok(cnt[L-1], str(i), ineq[L-1]):
            check[i] = True
            go(L+1, cnt+str(i))
            # cn
            check[i] = False
# check 배열만들어서 하나씩 지움
check = [0] * 10
n = int(input())
# 0은 '>' 1은 '<'로 설정
ineq = input().split()
# print(ineq)

data=[]
go(0, "")
data.sort()
print(data[-1])
print(data[0])


