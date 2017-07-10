# http://www.ccs.neu.edu/home/jaa/CS7800.12F/Information/Handouts/dyn_prog.pdf
# http://interactivepython.org/courselib/static/pythonds/Recursion/DynamicProgramming.html

# Problem 31
 
coins = [1, 2, 5, 10, 20, 50, 100, 200]
change = 200
ways = [1] + [0]*change

for coin in coins:
    for i in range(change-coin+1):
        ways[i+coin] += ways[i]

print(ways[-1])

# Prpblem 76

num = [n for n in range(1, 101)]
com = [1] + [0]*100

for n in num:
    for idx in range(101-n):
        com[n + idx] += com[idx]
        
print(com[-1])

# Problem 77

def prime_sieve(n):
    primes = [True]*n
    for num in range(3,int(n**(1/2)), 2):
        if primes[num]:
            primes[num*num:n:2*num] = [False]*int((n-num*num-1)/(2*num) + 1)
    return [2] + [i for i in range(3, n, 2) if primes[i]]

primes = prime_sieve(100)
found = False
limit, guess = 5000, 10

while not found:
    L = [1] + [0]*guess
    P = [d for d in primes if d < guess]
    for p in P:
        for j in range(guess-p+1):
            L[p + j] += L[j]
    if L[-1] < limit:
        guess += 1
    else:
        found = True
    
print(guess)

