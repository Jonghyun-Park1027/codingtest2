# 모르는 친구랑 게임하면 무조건 짐
# 몇몇 플레이어랑 게임하면 게임의 승패를알 수 있음
# 0 밑으론 안떨어짐
# N번째 게임에서 탈출하면 I'm not ironman 툴출 못하면 i am ironman
# G(점수)를 달성하고 N 내에서 탈출하면 끝 이후엔 져도 상관없다
# 탈출하기 위해 G가 커지면 탈출못할 수도 있음

# from collections import Counter

N, P = map(int, input().split())  # N 게임 횟수 P 플레이어 정보 수 <1000
W, L, G = map(
    int, input().split()
)  # W 이길때 점수, L 질떄 점수, G iron 벗아나기 위한 점수

hack = dict()
for i in range(P):
    cnt_n, cnt_w = input().split()
    hack[cnt_n] = cnt_w
num = 0
for j in range(N):
    target = input()
    if hack.get(target) == None or hack[target] == "L":
        if num - L < 0:
            num = 0
        else:
            num -= L
    else:
        num += W
        if num >= G:
            print("I AM NOT IRONMAN!!")
            exit(0)

print("I AM IRONMAN!!")
