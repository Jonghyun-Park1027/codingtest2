'''
unsolved, 인덱싱 오류
# 3 <= n <= 50
unsolved
def search_all(graph, n):
    max_col = 0
    count_col = 0
    max_row = 0
    count_row = 0
    data = []
    # 가로 같은 문자열 찾기
    for i in range(n-1):
        for j in range(n-1):
            if max_col == n:
                return max_col
            if graph[i][j] == graph[i][j+1] : 
                count_col += 1
            if max_row == n:
                return max_row
            if graph[j][i] == graph[j+1][i] : 
                count_row += 1
  
        max_col = count_col
        count_col = 1
        max_row = count_row
        count_row = 1
        data.append(max_col)
        data.append(max_row)
    return max(data)

n = int(input())
graph = [list(input()) for i in range(n)]

final_data = []
for i in range(n-1):
    for j in range(n-1):
        # 가로
        graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
        final_data.append(search_all(graph,n))
        graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
        # 세로
        graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]
        final_data.append(search_all(graph,n))
        graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]
print(max(final_data))'''
def search_all(graph, n):
    max_length = 0
    
    # 가로 검사
    for i in range(n):
        count = 1
        for j in range(1, n):
            if graph[i][j] == graph[i][j-1]:
                count += 1
                max_length = max(max_length, count)
            else:
                count = 1
    
    # 세로 검사
    for j in range(n):
        count = 1
        for i in range(1, n):
            if graph[i][j] == graph[i-1][j]:
                count += 1
                max_length = max(max_length, count)
            else:
                count = 1
    
    return max_length

# Sample Test
n = int(input())
graph = [list(input()) for i in range(n)]

final_data = []
for i in range(n):
    for j in range(n-1):
        # 가로
        graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
        final_data.append(search_all(graph, n))
        graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
        
        # 세로
        graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]
        final_data.append(search_all(graph, n))
        graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]

print(max(final_data))
