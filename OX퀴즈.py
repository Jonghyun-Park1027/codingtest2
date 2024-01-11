n = int(input())
for _ in range(n):
    num = 0
    answer = 0
    g = list(input())

    while g :
        a = g.pop()
        if a == "O":
            num += 1
            answer += num
            
        else :
            num = 0
    print(answer)