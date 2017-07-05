def fact(n):
    if n == 1:
        return n
    return n*fact(n - 1)

def binom(n, r):
    return fact(n)//fact(r)//fact(n - r)

s = 0
for m in range(23, 101):
    for l in range(2, m):
        if binom(m, l) > 10**6:
            s += 1
        
print(s)
