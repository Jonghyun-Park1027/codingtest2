n = int(input())
card = [0]+ list(map(int,input().split()))
pay = [-1] * (n+1)

pay[0] = 0
for i in range(1,n+1):
    for j in range(1, i+1):
        if pay[i] == -1 or pay[i] > pay[i-j] + card[j]:
            
            pay[i] = pay[i-j] + card[j]

print(pay[n])