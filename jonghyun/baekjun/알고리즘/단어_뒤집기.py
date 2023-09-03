n = int(input())

for _ in range(n):
    t = input().split()
    answer = []
    for i in t:
        # print(i[::-1])
        
        answer.append(i[::-1])
    print(" ".join(answer))
    # print(answer)