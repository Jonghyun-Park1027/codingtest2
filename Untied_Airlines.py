from collections import Counter


def cal(s):
    cal_dict = {
        "L": 120,
        "S": 150,
        "B": 150,
        "N": 40,
        "C": 160,
        "D": 100,
        "R": 100,
        "O": 100,
    }
    return cal_dict.get(s, 0)


while True:
    word = input()
    if word == "#":
        break
    num = 0
    if word[0] == "U":
        numcounter = Counter()
        while True:

            seat = input().split()
            if len(seat) != 2:
                break

            seat, n = seat
            n = cal(n)

            numcounter[seat] += n

        for i in numcounter:
            if numcounter[i] >= 200:

                num += 1

    print(f"{word} {num}")
