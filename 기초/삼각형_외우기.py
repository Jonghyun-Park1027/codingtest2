def cal(a,b,c):
    if a == b and b== c:
        return "Equilateral"
    elif a+b+c == 180:
        if a==b or b==c or a==c :
            return "Isosceles"
        else :
            return "Scalene"
    else :
        return "Error"
data = []
for i in range(3):
    data.append(int(input()))
a, b, c = data
print(cal(a,b,c))