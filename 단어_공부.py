from collections import defaultdict
n = list(map(lambda x : x.upper(), input()))
d = defaultdict(str)

for i in n :
    if d[i] :
        d[i] += 1
    else :
        d[i] = 1

answer = max(d.values())

counter = 0

for i in d :
    if d[i] == answer :
        counter += 1
        if counter >= 2:
            print("?")
            break
if counter == 1:
    print(max(d, key=d.get))