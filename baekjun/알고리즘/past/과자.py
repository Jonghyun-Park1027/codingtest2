snack, n, a = map(int,input().split())
answer = snack*n - a
if answer <=0 :
    answer = 0
print(answer)
