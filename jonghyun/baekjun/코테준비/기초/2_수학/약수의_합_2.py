n = int(input())

# def cal_1(n):
#     target = int(n **0.5)

#     answer = 0
#     for i in range(1, target+1):
        
#         if n % i == 0 and i**2 != n:
#             answer += i
#             answer+= n//i

#         elif i**2 == n:
#             answer+=i        
#     return answer

answer = 0
for i in range(1,n+1):
    answer += n//i*i

    answer

print(answer)
