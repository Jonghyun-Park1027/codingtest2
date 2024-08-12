t= int(input())

for _ in range(t):
    g = input().split()
    n = float(g[0])
    for i in range(len(g)):
        if i == 0 :
            continue
        if g[i] == "@":
            n *= 3
        elif g[i] == "%":
            n += 5
        else :
            n -= 7
    print(f"{n:.2f}")