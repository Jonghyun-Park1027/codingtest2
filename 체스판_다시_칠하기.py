# 완성된 판 만들기

g_1 = ('WB'*4+'BW'*4)*4
g_2 = ('BW'*4+'WB'*4)*4

# 완성된 판에 따른 정답수 계산하기
a_1 = 0
a_2 = 0

# 가장 작은수를 쓸 answer만들기
answer = 64

n, m = map(int,input().split())


t = []
for _ in range(n):
    t.append(input())

# print("".join(t))
t = "".join(t)
# print(len(t))
for i in range(m):
    data =
    print(data)
    # for i in range(64):
    #     if g_1[i] != data[i] :
    #         a_1 += 1
    #     if g_2[i] != data[i] :
    #         a_2 += 1
        # if 
    # print("a_1 :", a_1)
    # print("a_2 :", a_2)
    # answer = min(answer,a_1,a_2)
#     answer = min(answer, a_1, a_2)
#     a_1 = 0
#     a_2 = 0
#     # print(answer)
# print(answer)