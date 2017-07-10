# https://en.wikipedia.org/wiki/Partition_(number_theory)#Generating_function

divisor = 10**6
found = False
guess = 0

L1 = [int(i*(3*i - 1)/2) for i in range(1, 200)]
L2 = [int(i*(3*i + 1)/2) for i in range(1, 200)]
n = sorted(L1 + L2)
sign = [1, 1, -1, -1]
part = [1]

while not found:
    guess += 1
    part += [0]
    s, idx = 0, 0
    # P = [num for num in n if num <= guess]
    # for p in P:
    #   s += sign[idx % 4]*part[guess - p]     
    while n[idx] <= guess:
        s += sign[idx % 4]*part[guess - n[idx]]
        idx += 1
    part[guess] = s
    if s % divisor == 0:
        found = True
        
print(guess)
