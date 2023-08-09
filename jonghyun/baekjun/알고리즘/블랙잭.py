''' 정인이 버전 블랙잭은 양의 정수 카드 - 딜러는 n장의 카드를 보이도록 바닥에 - 딜러가 숫자 m을 외침
- 플레이어는 제한된 시간에 n장중 3장을 고름 - 플레이어의 카드 합은 m을 넘지않고 m과 최대한 가깝게
- n 장의 카드를 통해 숫자 m이 주어질 경우 m에 최대한 가깝게


'''
'''
오답
n, m = map(int, input().split()) # n은 카드 수, m은 목표값
card_num = list(map(int,input().split())) # 카드의 종류

def cardsum(pick,data):
    for target in data :
        current = target
        if pick+current <= m :
            

            return cardsum(pick+current,data)
    else:
        return pick
answer = []
# for _ in range(3):
# for i in card_num:

for i in range(3):

    answer.append(cardsum(card_num[i], card_num))

print(answer)

# 카드를 순서대로 뽑아서 경우의 수를 고려한다

''' 
#풀이
# n은 100개까지만 가능. 3개만 뽑는다. 조합(C(n,3)) = n(n-1)(n-2)/ 3! 대충 1,000,000 연산이라 치면 
# 컴퓨터에서 가능함 2천만 미만까지가 시간초과 안될확률높음
n, m = map(int, input().split()) # n은 카드 수, m은 목표값
card_num = list(map(int,input().split())) # 카드의 종류

result = 0
length = len(card_num)

count = 0
for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j + 1, length):
            sum_value = card_num[i] + card_num[j] + card_num[k]
            if sum_value <= m:
                result = max(result, sum_value)
print(result)

