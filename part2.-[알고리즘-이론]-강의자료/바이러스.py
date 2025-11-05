from collections import defaultdict

t = int(input())

n = int(input())

graph = defaultdict(set)

for _ in range(n):
    A, B = map(int, input().split())
    graph[A].add(B)
    graph[B].add(A)

# print(graph)
# for i in graph:
#     for j in graph[i]:
#         print(j)


def BFS(graph):
    visit = []
    need_visit = []

    need_visit.append(1)
    while need_visit:
        cnt = need_visit.pop()
        if cnt in visit:
            continue
        visit.append(cnt)
        for i in graph[cnt]:
            need_visit.append(i)
        # print(visit)

    return len(visit) - 1


print(BFS(graph))
