import sys

# 입력 처리
input = sys.stdin.readline

# 문자 구분자 + 숫자 구분자 합치기
n = int(input())
delimiters = set(input().split())

m = int(input())
delimiters.update(input().split())

# 병합자는 구분자에서 제거
k = int(input())
mergers = input().split()
for ch in mergers:
    delimiters.discard(ch)

_ = int(input())  # 문자열 길이 입력 (무시)
input_string = input().rstrip()
# print(input_string)
# 문자열 분할
result = []
word = ""
for c in input_string:
    if c in delimiters or c == " ":
        if word:
            result.append(word)
            word = ""
    else:
        word += c
        # print(word)
# 마지막 단어 추가
if word:
    result.append(word)

# 결과 출력
print("\n".join(result))
