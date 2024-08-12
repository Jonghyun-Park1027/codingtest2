n = int(input())
MAX = 1001
ans  = [0] * MAX

ans[0] = 1
ans[1] = 3
# ans[2] = 5

for i in range(2, MAX):
    ans[i]= 2*(ans[i-2])+ans[i-1]

print(ans[n-1]%10007)
# print(ans)