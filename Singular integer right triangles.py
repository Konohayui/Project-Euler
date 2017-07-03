# http://mathforum.org/dr.math/faq/faq.pythag.triples.html

triples = {}
L = 1500000

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

for m in range(2, int((L)**0.5)+1):
    for n in range(1, m):
        if gcd(m,n) == 1:
            x, y, z = m**2 - n**2, 2*m*n, m**2 + n**2
            s = x + y + z
            d = 1
            while d*s <= L:
                l = d*s
                if l in triples:
                    t = sorted([x*d, y*d, z*d])
                    if t not in triples[l]:
                        triples[l] += [t]
                else:
                    triples[l] = [sorted([x*d, y*d, z*d])]
                d += 1


result = 0
for e in triples:
    if len(triples[e]) == 1:
        result += 1
        
print(result)
