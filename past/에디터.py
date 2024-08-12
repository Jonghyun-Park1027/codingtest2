# 최대 글자수 600,000
# 시간복잡도를 고려할 때 이중 O(1)의 접근법 필요

# left, right 스택 만들기
# left의 최대입력 100,000
import sys
input = sys.stdin.readline
left = list(input())[:-1]
right = []

t = int(input())

for _ in range(t):
    a, *b = input().split()

    if len(b) == 1:
# P $ $라는 문자를 커서 왼쪽에 추가
        left.append(b[0])
# L 커서를 왼쪽으로 한칸
    elif a == "L":
        if len(left) == 0 :
            continue
        s = left.pop()
        right.append(s)
# D 커서를 오른쪽으로 한칸
    elif a == "D":
        if len(right) == 0 :
            continue
        s = right.pop()
        left.append(s)
# B 커서 왼쪽문자를 삭제
    elif a == "B":
        if len(left) == 0 :
            continue
        left.pop()

# 뒤집어서 원래 순열을 만듦
right = right[::-1]
# print(left)
# print(right)
print("".join(left+right))