a, b, c = map(int,input().split())

d= int(input())
d = c+d
s = 60
m = s*60
h = m*24
while d > 59 :
    d -= 60
    b += 1
    if b >= 60:
        b = 0
        a += 1
    if a >= 24:
        a = 0
# if d >= 60 :
    # d = 0
    # b += 1
# print("a :", a)
# print("b :", b)
# print("c :", c)
# print("d :", d)
print(a, b, d)