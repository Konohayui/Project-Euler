def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

trip = {}
P = 1000

for m in range(3, 100):
    for n in range(1, m):
        if gcd(m,n) == 1:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            s = a + b + c
            d = 1
            while d*s <= P:
                t = sorted([d*a, d*b, d*c])
                if d*s in trip:
                    if t not in trip[d*s]:
                        trip[d*s] += [t]
                else:
                    trip[d*s] = [t]
                d += 1
                    
                    
L = {}
for p in trip:
    L[len(trip[p])] = p
    
print(L[max(L)])
