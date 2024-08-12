import hashlib
t = input()

ans = hashlib.sha256(t.encode()).hexdigest()
print(ans)