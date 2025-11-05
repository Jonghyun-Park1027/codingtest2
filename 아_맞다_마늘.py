import sys

input = sys.stdin.read
data = input().split("\n")
# print(data)
N = int(data[0].strip())
a = set(data[1].split())
b = set(data[2].split())
print(*(a - b))
