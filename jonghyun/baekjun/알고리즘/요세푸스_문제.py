import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())
# graph = [i for i in range(1, n+1)]
graph = deque()
for i in range(1, n+1):
    graph.append(i)
# count = k
# count= 0
# while graph :

#     for i in range(len(graph)):
#         count += 1
#         if count == k :
#             # print(graph, count)
#             print(graph[i])
#             del graph[i]
#             count = 0
answer = []
count = 0
# def loop(graph):
#     global count
    # if not graph :
    #     return
while graph :
    # idx += 1
    count += 1
    graph.append(graph.popleft())
    if k  == count :
        # print(graph)
        answer.append(graph.pop())
        count = 0

# loop(graph)
print("<"+", ".join(map(str,answer))+">")

