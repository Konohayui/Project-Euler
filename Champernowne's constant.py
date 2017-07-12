L = []
for n in range(0,1000000):
    L += [s for s in str(n)]

result = 1
for n in range(1,7):
    result *= int(L[10**n])
    
print(result)
