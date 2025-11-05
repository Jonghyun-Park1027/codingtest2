# 팰린드롬은 그냥 단어를 뒤집으면 됨
# 미러는 거울에 비친것처럼 3과 E는 reverse가 됨 이는 미러임
# 미러 팰린드롬은 위 두 조건을 둘다 만족함


mirror_map = {
    "A": "A",
    "E": "3",
    "H": "H",
    "I": "I",
    "J": "L",
    "L": "J",
    "M": "M",
    "O": "O",
    "S": "2",
    "T": "T",
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
    "Y": "Y",
    "Z": "5",
    "1": "1",
    "2": "S",
    "3": "E",
    "5": "Z",
    "8": "8",
}


def cal(c1, c2):
    return mirror_map.get(c1, "") == c2


while True:
    palindrome = True
    mirror = True
    try:
        s = input()
    except EOFError:
        break
    compare = s[::-1]
    n = len(s)
    for i in range(n):
        if palindrome:
            if s[i] != compare[i]:
                palindrome = False
        if mirror:
            # print(f"s[i] : {s[i]}, compare[i] : {compare[i]}")
            mirror = cal(s[i], compare[i])

    if mirror and palindrome:
        print(f"{s} -- is a mirrored palindrome.\n")
    elif not mirror and palindrome:
        print(f"{s} -- is a palindrome.\n")
    elif mirror and not palindrome:
        print(f"{s} -- is a mirrored string.\n")
    else:
        print(f"{s} -- is not a palindrome.\n")
