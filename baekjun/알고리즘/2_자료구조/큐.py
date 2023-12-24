import sys

# 명령의 수 n
input = sys.stdin.readline


# 시작점과 끝점 정하기
start = 0
end = 0

# 테케의 수 t

t= int(input())

# 숫자 리스트의 최대 크기는 100,000이다
q = [-1] * (t+1)
# 출력할땐 앞자리를 더하고 빼낼떈 뒷자리를 더한다
for _ in range(t):
    a, *b = input().split()
    # print(a,b)

    if a == "push" :
        end += 1
        q[end-1] = int(b[0])
        # start += 1
    elif a == "pop" :
        if q[start] == -1:
                print(-1)
                continue
        print(q[start])

        q[start] = -1
        start += 1    
    elif a == "size":
        print(end - start)
    elif a == "empty":
        if end - start == 0:
            print(1)   
        else :
            print(0)
    elif a == "front":
        print(q[start])
    elif a == "back":
        print(q[end-1])    
    # print(q)
    # print("act :", a)
    # print("start :", start)
    # print("end : ", end)
# print(q[:end])