# from collections import defaultdict

L, G, R = map(int, input().split())  # L : 램프 수 , G : 경비 수, R : 순찰 횟수
g = dict()  # 아조씨들 끄는 순번 담을 딕셔너리
lamp = [False for i in range(L + 1)]
for _ in range(G):
    n, start, term = input().split()
    start = int(start)
    term = int(term)
    g[n] = [i for i in range(start, L + 1, term)]  # 순번 리스트 g딕셔너리에 저장
    # print(g[n])
for _ in range(R):  # 반복회수만큼 아조씨들 소환
    n = input().strip()
    # print(n)
    for i in g[n]:
        lamp[i] = not lamp[i]
        # print(lamp)
print(sum(lamp))
