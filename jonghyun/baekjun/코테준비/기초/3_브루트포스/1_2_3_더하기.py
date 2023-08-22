# 1, 2, 3의 합
n = int(input())
for _ in range(n):
    m = int(input())
    # if m == 1 :
    #     print(1)
    #     continue
    answer = 0
    for a in range(1,4):
        if a == m:
            answer += 1
        for b in range(1,4):
            if a+b == m:
                answer += 1
                # continue
            for c in range(1,4):
                if a+b+c == m:
                    answer += 1
                for d in range(1,4):
                    if a+b+c+d == m:
                        answer +=1
                    for e in range(1,4):
                        if a+b+c+e+d==m:
                            answer +=1

                        for f in range(1,4):
                            if a+b+c+d+e+f == m:
                                answer +=1
                            for g in range(1,4):
                                if a+b+c+d+e+f+g == m:
                                    answer +=1
                                for h in range(1,4):
                                    if a+b+c+d+e+f+g+h == m:
                                        answer +=1
                                    for i in range(1,4):
                                        if a+b+c+d+e+f+g+h+i == m:
                                            answer += 1
                                        for j in range(1,4):
                                            if a+b+c+d+e+f+g+h+i+j == m:
                                                answer += 1
    print(answer)