import sys

data = {1: "c", 2: "d", 3: "e",4: "f",5: "g",6: "a",7: "b",8: "C"}

asc = ["c","d","e","f","g","a","b","C"]

dsc = ["C","b","a","g","f","e","d","c"]

t = list(map( int,input().split()))

ans = [data[i] for i in t]

if ans == asc: 

    print("ascending")

elif ans == dsc: 

    print("descending")

else: 

    print("mixed")