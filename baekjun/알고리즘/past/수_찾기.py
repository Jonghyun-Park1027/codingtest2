import sys
input = sys.stdin.readline

n = int(input())
n_g = input().split()
n_g_d = dict()

for i in n_g:
    # if n_g_d[i] == 1:
    #     n_g_d[i] += 1
    n_g_d[i] = 1
# print(n_g_d)
m = int(input())
m_g = input().split()
for i in m_g:
    if n_g_d.get(i):
        print(1)
    else :
        print(0)