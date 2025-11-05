# 군대를 보낼때 우리나라 군대라고 안하고 숫자 군대로 명칭
# 어느 땅에서 한 번호의 군대 병사가 절반을 초과하면 점령당한것
# 각 땅의 절반 이상을 차지한 군대의 번호를 출력, 아직 절반 이상이 아니면 SYJKGW 출력
from collections import Counter

N = int(input())  # 땅의 개수
for _ in range(N):

    land = list(map(int, input().split()))
    ti, s = land[0], land[1:]

    answer = True
    goal = int(ti / 2)

    g = Counter(s)

    if g.most_common(1)[0][1] > goal:
        print(g.most_common(1)[0][0])
        answer = False

    if answer == False:
        continue
    else:
        print("SYJKGW")
