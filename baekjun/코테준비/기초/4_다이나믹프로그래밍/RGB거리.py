
n = int(input())
a = [(0,0,0)] + [tuple(map(int,input().split())) for _ in range(n)]
d = [[0,0,0] for _ in range(n+1)]
for i in range(1, n+1):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + a[i][0];
    d[i][1] = min(d[i-1][0], d[i-1][2]) + a[i][1];
    d[i][2] = min(d[i-1][0], d[i-1][1]) + a[i][2];
print(min(d[n][0], d[n][1], d[n][2]))
# n = int(input())

# data = []
# for _ in range(n):
#     data.append(list(map(int,input().split())))
# check = [[0] * 3 for _ in range(n)]
# answer =0
# target = data[0].index(min(data[0]))
# check[0][target] = 1
# answer += min(data[0])
# if data[0][1] == data[0][2] or data[0][0] == data[0][1] or data[0][2] == data[0][0]:
#     target = -1

# if 0 == target :
#     if data[1][1] == data[1][2] :
#         target = -1
#         answer += data[1][1]
        
#     # print("0", min(data[1][1], data[1][2]))
#     answer_a = min(data[1][1], data[1][2])
#     answer += answer_a
#     check[1][target] = 1
#     target = data[1].index(answer_a)
# elif 1 == target :
#     # print("1", min(data[1][1], data[1][2]))
#     if data[1][0] == data[1][2] :
#         target = -1
#         answer += data[1][0]
#     answer_a = min(data[1][0], data[1][2])
#     answer += answer_a
#     check[1][target] = 1
#     target = data[1].index(answer_a)
# elif 2 == target :
#     if data[1][0] == data[1][1] :
#         target = -1
#         answer += data[1][0]
#     # print("2", min(data[1][1], data[1][2]))
#     answer_a = min(data[1][0], data[1][1])
#     answer += answer_a
#     check[1][target] = 1
#     target = data[1].index(answer_a)
# elif -1 == target :
#     # print("2", min(data[i][1], data[i][2]))
#     answer_a = min(data[i])
#     target = data[i].index(answer_a)
#     answer += answer_a
#     check[i][target] = 1

# print(target)
# for i in range(2, n):
#     target = 
# for i in range(1, n):
#     if 0 == target :
#         if data[i][1] == data[i][2] :
#             target = -1
#             answer += data[i][1]
#             continue
#         # print("0", min(data[i][1], data[i][2]))
#         answer_a = min(data[i][1], data[i][2])
#         answer += answer_a
#         check[i][target] = 1
#         target = data[i].index(answer_a)
#     elif 1 == target :
#         # print("1", min(data[i][1], data[i][2]))
#         if data[i][0] == data[i][2] :
#             target = -1
#             answer += data[i][0]
#         answer_a = min(data[i][0], data[i][2])
#         answer += answer_a
#         check[i][target] = 1
#         target = data[i].index(answer_a)
#     elif 2 == target :
#         if data[i][0] == data[i][1] :
#             target = -1
#             answer += data[i][0]
#         # print("2", min(data[i][1], data[i][2]))
#         answer_a = min(data[i][0], data[i][1])
#         answer += answer_a
#         check[i][target] = 1
#         target = data[i].index(answer_a)
#     elif -1 == target :
#         # print("2", min(data[i][1], data[i][2]))
#         answer_a = min(data[i])
#         target = data[i].index(answer_a)
#         answer += answer_a
#         check[i][target] = 1
#     # # print(target)
#     # if i == n-1 :
#     #     if check[0].index(min(check[0])) == check[n-1].index(min(check[n-1])):
#     #     print(target)

# print(answer)