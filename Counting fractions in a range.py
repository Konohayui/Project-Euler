def gcd(a,b):
    while b:
        a, b = b, a % b
    return a 

d, count = 12000, 0

for m in range(5, d+1):
    for n in range(1,m):
        if 1/3 < n/m < 1/2 and gcd(m,n) == 1:
            count += 1
            
print(count)
