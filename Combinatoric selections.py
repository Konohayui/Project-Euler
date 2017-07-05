def fact(n):
    if n == 1:
        return n
    return n*fact(n - 1)

def binom(n, r):
    return fact(n)//fact(r)//fact(n - r)

s = 0
for n in range(23, 101):
    for r in range(2, m):
        if binom(n, r) > 10**6:
            s += 1
        
print(s)
