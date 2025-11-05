from collections import Counter


while True:
    target_a, target_b = input().split()
    if target_a == "0" and target_b == "0":
        break
    a_g = Counter()
    b_g = Counter()
    a_g[target_a] += 1
    b_g[target_b] += 1

    num = 0
    a = target_a
    b = target_b
    while True:

        temp = 0
        for i in a:
            temp += int(i) ** 2

        temp = str(temp)

        if a_g[temp] == 0:

            a_g[temp] = a_g[a] + 1
        else:

            break
        a = temp

    while True:
        if a_g[b] != 0:  # b가 a의 수열에 있다면 meeting!
            num = a_g[b] + b_g[b]
            break
        temp = 0
        for j in b:
            temp += int(j) ** 2
        temp = str(temp)
        if b_g[temp] != 0:
            # 이미 b의 수열에 temp가 있으므로
            # temp가 공통 숫자인지 다시 확인한 후 break
            if a_g[temp] != 0:
                num = a_g[temp] + b_g[b] + 1
            break
        b_g[temp] = b_g[b] + 1
        b = temp

    print(f"{target_a} {target_b} {num}")
