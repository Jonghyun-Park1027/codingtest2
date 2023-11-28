from itertools import combinations
while True:
    n, *data = list(map(int, input().split()))
    # print(n, data)
    answer = list(combinations(data, 6))
    for i in answer:
        print(*i)
    print()
    if not data:
        break
