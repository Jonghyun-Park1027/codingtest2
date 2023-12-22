MAX = 1000000
check = [0 for i in range(MAX+1)]
graph = [i for i in range(MAX+1)]

check[0] = check[1]= 1

for i in graph:
    if not check[i]:
        num = i
        
        while i+num < MAX:
            i += num
            check[i] = True
            #

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n+1):
        if i*i > MAX:
            print("Goldbach's conjecture is wrong.")
            break
        elif not check[i]:
            if not check[n-graph[i]] and n == graph[i]+graph[n-graph[i]]:
                print(f"{n} = {graph[i]} + {graph[n-graph[i]]}")
                break
