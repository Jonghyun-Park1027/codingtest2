# import re
a = int(input())
b = int(input())
c = int(input())

t = str(a*b*c)
answer = {}
for i in range(10):
    answer[str(i)] = 0

# mask = '[0-9]'
# for i in t :
    # print(re.findall(mask, i))
for i in t:
    answer[i] += 1

for i in answer:
    print(answer[i])