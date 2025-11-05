while True:
    n, m = map(int, input().split())
    if n == m == 0:
        exit(0)
    if n <= m:
        print("No")
    else:
        print("Yes")
