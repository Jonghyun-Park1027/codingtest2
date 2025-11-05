import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()
M = int(input())
M_list = list(map(int, input().split()))
# m_list.sort()


def binary_search(n, start, end):
    if start > end:
        return False
    middle = (start + end) // 2

    if N_list[middle] > n  :
        return binary_search(n, start, middle -1)
    elif N_list[middle] < n :
        return binary_search(n, middle+1, end)
    else :
        return True
for i in M_list:
    if binary_search(i, 0, N-1):
        print(1)
    else :
        print(0)
