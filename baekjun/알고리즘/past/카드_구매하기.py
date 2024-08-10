t = int(input())

cardpack = [0]+list(map(int,input().split()))

# print(cardpack)

ans = [0] * (t+1)
for i in range(1, t+1):

    for j in range(1,i+1):
        
        ans[i] = max(ans[i], ans[i-j]+cardpack[j])
print(ans)  