import string
from collections import defaultdict

n = int(input())
g = list(input())
uppercase = dict.fromkeys(list(string.ascii_uppercase), 0)
uppercase_key = list(uppercase)
# uppercase = ]
left = []
right = []
# print(uppercase_key)
for i in range(n):
    cnt = int(input())
    uppercase[uppercase_key[i]] = cnt


def cal(a, b, t):
    if t == "*":
        return a * b
    elif t == "+":
        return a + b
    elif t == "/":
        return a / b
    elif t == "-":
        return a - b


# print(uppercase)
# print(cal(1, 1, "*"))
for i in g:
    if i not in uppercase:
        a = right.pop()
        b = right.pop()
        right.append(cal(b, a, i))
        # print(right)
        # print(1)
    else:
        right.append(uppercase[i])
        # print(right)
        # print(cal(uppercase[i], uppercase[i], "*"))
print(f"{right[-1]:.2f}")
