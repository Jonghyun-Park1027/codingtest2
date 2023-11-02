a, b = map(int, input().split())
def GCD(a,b):
    if b == 0 :
        return a
    
    return GCD(b, a%b)

gcd = GCD(a,b)
print(gcd)
print(int(gcd*(a/gcd)*(b/gcd)))