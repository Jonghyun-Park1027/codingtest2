import sys
input = sys.stdin.readline
n = int(input())

right = []
answer = []
# 입력을 받는다
t = [int(input()) for _ in range(n)]

#입력값
counter = 0
for i in range(n):
    if counter < t[i]:
        while counter < t[i]:
            counter += 1
            answer.append("+")
            right.append(counter)
        right.pop()
        answer.append("-")
    else :
        if right[-1] != t[i]:
            print("NO")
            sys.exit(0)
        right.pop()
        answer.append("-")




print(*answer, sep="\n")