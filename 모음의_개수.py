while True:
    t = input()
    if t == "#":
        break
    t = list(t)
    t = [i for i in t if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]]
    print(len(t))
