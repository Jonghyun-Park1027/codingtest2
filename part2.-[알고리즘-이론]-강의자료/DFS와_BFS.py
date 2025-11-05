from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = {}
for i in range(1, n+1):
    graph[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 모든 인접 리스트를 미리 오름차순으로 정렬합니다.
for i in range(1, n+1):
    graph[i].sort()

def DFS(graph, v):
    visit = []
    stack = [v]

    while stack:
        cnt = stack.pop()
        if cnt not in visit:
            visit.append(cnt)
            # 스택에 다음 노드를 추가할 때 역순으로 추가해야 DFS에서
            # 작은 노드가 먼저 나오게 됩니다.
            for i in reversed(graph[cnt]):
                if i not in visit:
                    stack.append(i)
    return visit

def BFS(graph, v):
    visit = []
    queue = deque([v])

    while queue:
        cnt = queue.popleft()
        if cnt not in visit:
            visit.append(cnt)
            # 큐에는 오름차순 그대로 추가합니다.
            for i in graph[cnt]:
                if i not in visit:
                    queue.append(i)
    return visit

# 결과 출력
print(*DFS(graph, v))
print(*BFS(graph, v))
