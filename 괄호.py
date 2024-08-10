n = int(input())


# print(g)
for _ in range(n):
    g = list(input())
    left = 0
    right = 0
    for i in g:
        if i == "(":
            left += 1
        else:
            # print(i)
            right += 1

# 오른쪽 괄호가 왼쪽괄호보다 많아질때 no
        if right > left:
            print("NO")
            break
# 나머지 yes
    if right == left :
        print("YES")
# 왼쪽괄호와 오른쪽 괄호가 숫자가 같지않을때 no
    elif left > right:
        print("NO")
    # print(left, right)
