def cal(a,b,c):
    data = [a,b,c]
    sumdata = 0
    max_a_idx= data.index(max(data))
    
    for i in range(3):
        if i != max_a_idx:
            sumdata += data[i]
            # print(i, data[i], data, max_a_idx)
    if max(data) >= sumdata:
        # print(max(data), data, sumdata)
        return "Invalid"
    elif a == b and b== c:
        return "Equilateral"

            
        
  


    elif  a==b or b==c or a==c :
        return "Isosceles"
    
    else :
        return "Scalene"
    
while True :
    
    a,b,c = map(int,input().split())
    if a ==0 and b ==0 and c ==0 :
        break
    elif a == 0 or b ==0 or c == 0 :
        print("Invalid")
        continue
    print(cal(a,b,c))
