t= int(input())

for _ in range(t):
    data = input()
    # print(data)
    answer = 0
    check = 1
    for i in data:
        if answer == -1 :
            check = 0
            print("NO")
            break
        elif i == '(' :
            answer += 1
        else :
            answer -= 1
    if check == 1:
        if answer == 0:
            print("YES")
        else :
            print("NO")