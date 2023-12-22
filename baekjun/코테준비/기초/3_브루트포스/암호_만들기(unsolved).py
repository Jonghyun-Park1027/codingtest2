'''# 소문자 L, 암호 길이 C
L, C = map(int,input().split())
# 모음
L_g = ["a","e","i","o","u"]
data = sorted(input().split())
# check
check = [0] * C
# continue용 배열 설정
arr = [0] * 200
answer = []
for i in L_g:
    arr[ord(i)] = 1
print(data)
# def 함수 선언
def DFS(answer ,L, C, arr, g_count):
    # global answer
    # start가 L과 같아진다면 return
    if len(answer) == L:
        print("".join(answer))
        return
    # data에 for문을 돌리고 arr[ord(i)]가 1일 경우 continue
    for i in range(C):
        if arr[ord(data[i])] and L- g_count <= 1 :
            # g_count += 1 
            # print(data[i])
            continue
        # if L - g_count <= 2:
        if arr[ord(data[i])] == 1:
            # print(ord(data[i]), data[i])
            g_count += 1
        #     print(g_count)
        #     answer.append(data[i])
            
        #     continue
            # continue
        if check[i]:
            continue
        # cnt가 true일때 자음만 append하기
        check[i] = True
        answer.append(data[i])
        DFS(answer, L,C, arr, g_count)
        answer.pop()
        check[i] = False
# for data[i] in range(C):

DFS(answer,L, C,arr, 0)'''


def check(password):
    ja = 0
    mo = 0
    for x in password:
        if x in 'aeiou':
            mo += 1
        else :
            ja += 1
    return ja >=2 and mo >= 1

def DFS(n, alpha, password, i):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    DFS(n, alpha, password+alpha[i], i+1)
    DFS(n, alpha, password, i +1)
n, m = map(int,input().split())
a = input().split()
a.sort()
DFS(n, a, "", 0)