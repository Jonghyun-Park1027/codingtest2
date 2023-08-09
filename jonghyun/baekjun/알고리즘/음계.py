# 배열 구현
harmony = {1 : "c", 2 : "d", 3 : "e", 4 : "f", 5 : "g", 6:"a", 7: "b", 8:"C"}
data = list(map(int, input().split()))
data_l = [harmony[i] for i in data]
if [harmony[i] for i in list(range(1,len(harmony)+1))] == data_l:
    
    print("ascending")
elif [harmony[i] for i in list(range(len(harmony),0, -1))]== data_l:
    
    print("descending")
else:
    print("mixed")
