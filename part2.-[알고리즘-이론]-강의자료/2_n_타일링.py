n = int(input())

def cal(n):
    if n <= 2:
        return n
    else:
        g = [0] * (n+1)
        g[1] = 1
        g[2] = 2
        for i in range(3, n+1):
            g[i] = g[i-1] + g[i-2]
        # print(g)   
        return g[n]

print(cal(n)%10007)