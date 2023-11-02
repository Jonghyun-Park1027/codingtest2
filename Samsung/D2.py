T = int(input())

for i in range(T):
    data= list(map(int, input().split()))
    odd_data = [num for num in data if num %2 == 1]
    #print("#"+f"{i+1} "+sum(odd_data))
    
    print(f"#{i+1} "+str(sum(odd_data)))