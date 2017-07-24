from math import factorial as fac

def digfac(n):
    s = 0
    for d in str(n):
        s += fac(int(d))
    return s

def chain(n):
    L = [n]
    idx = 0
    while True:
        c = digfac(L[idx])
        if c not in L:
            L.append(c)
            idx += 1
        else:
            return(L, idx + 1)

result, limit, chain_len = 0, 1000000, 60

for num in range(limit + 1):
    if chain(num)[1] == chain_len:
        result += 1
        
print(result)
