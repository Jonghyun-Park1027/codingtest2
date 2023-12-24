import sys
n = int(input())

# t는 만들어야할 원본, 따라해야할 원본
t = [int(input()) for _ in range(n)]

# t와 똑같이 만들어야 할 데이터
data = []

cnt = 0
answer = []
# num에서 하나씩 뽑아서 t와 대조해본다
for i in range(n):
    # 인덱스 기준으로 num과 i가 같지않다면 data에 넣고 +를 출력
    if cnt < t[i] :
        while cnt < t[i]:
            cnt += 1
            answer.append("+")
            data.append(cnt)
        data.pop()    
        answer.append('-')
    # 넣었는데 data에 넣은 마지막 숫자가 현재 t[i]와 같다면 하나씩 뺀다
    # i를 저장한다
        # print(data)
    
    else :
        if data[-1] != t[i]:

            print("NO")
            sys.exit(0)
        data.pop()
        answer.append("-")
# print(data)
# if data:
    # print("NO")

print(*answer, sep= "\n")