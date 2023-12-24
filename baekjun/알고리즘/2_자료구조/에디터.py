# 입력 빨리받기
import sys
input = sys.stdin.readline

# 여기서  insert는 많은 시간이 소요됨. 따라서 버린다. 근데 슬라이싱이 더오래걸리네;

# 문자열 N의 길이는 100,000 / 명령어의 개수는 총 500,000개 즉 for문이 안된다.
# input을 인덱싱을 위해 list화 한다
left = list(input().strip())
right = []


# 명령 갯수
t = int(input())

# 명령 입력 1회 받기(나중에 수정)
for _ in range(t):
    a, *b = input().split()


# 커서 위치는 총 문자열 길이 +1가지

    # L 은 왼쪽으로 한칸 옮기는데, 문장의 맨 앞이면 무시됨
    if a == "L" and left:
        d = left.pop()
        right.append(d)

#     # D 는 커서를 오른쪽으로 한칸 옮기는데, 문장의 맨 끝쪽이면 무시됨
    elif a == "D" and right:
        d = right.pop()
        left.append(d)

#     # B 는 커서 왼쪽의 문자를 삭제하는데, 문장의 맨 앞이면 무시됨
    elif a == "B" and left:
        # text = text[:cursor-1] + text[cursor:]
        left.pop()

#     # P $는 $ 라는 문자를 커서 왼쪽에 추가함
    elif b : # 입력문자가 존재할 경우
        # text[cursor] = b[0] # 현재 커서위치를 b 문자로 바꾼다
        # text = text[:cursor] + b + text[cursor:]
        left.append(b[0])

print(''.join(left +  right[::-1]))
