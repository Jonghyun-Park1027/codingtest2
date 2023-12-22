from collections import defaultdict
# 카드팩데이터를 외부에서 구현
t = int(input())
# 갱신용 max 데이터
answer = 0
card = defaultdict(int)

graph = [0] + list(map(int,input().split()))
# print(graph)
# for idx, value in enumerate(graph) :
#     card[idx] = value

# card = sorted(card.items(), reverse=True)
# print(card)
# check 카드 배열 만들기
check = [0] * (t+1)
for i in range(1, t+1):
    for j in range(1, i+1):
        check[i] = max(check[i], check[i-j]+graph[j])
print(check[t])
# print(check)
# t를 입력으로 받아 계속 감소시킴
# def calc(target):
#     global answer, t
#     # 카드 가격을 맞추면 return
#     if answer == t:
#         answer = max(cnt, answer)
#         return
#     cnt = 0
# # n은 카드 갯수, value는 카드팩 가격
#     for n, value in card :
#         n += 1
#         # print(n, value)
#         # print(t)
#         # 정수로 나뉘는 경우에만 나누고 나머지를 n에 분배
#         if t >= n :
#             t -= n
#             cnt += value
#             if t == 0:
#                 return
#             # print(answer)
#             # print(t/n)

# calc(0)
# print(answer)