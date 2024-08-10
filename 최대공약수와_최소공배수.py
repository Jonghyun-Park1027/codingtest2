a, b = map(int, input().split())

# print(a,b)

def GCD(a,b):
    if b == 0 :
        return a
    # print(a,b)
    return GCD(b, a%b)

gcd = GCD(a,b)
print(gcd)

lcm = gcd * (a/gcd) * (b/gcd)
print(int(lcm))

