# -*- coding: utf-8 -*-

# Generates all primes < n
def Prime(n):
    prem = [2,3,5]
    for i in range(7,n,2):
        b = True
        k = 0
        while i**0.5 >= prem[k] and b:
            if i % prem[k] == 0:
                b = False
            k += 1
        if b:
            prem.append(i)
    return prem

# Finds the nth prime
def NthPrime(n):
    prem = [2,3,5]
    i = 7
    while len(prem) < n:
        b = True
        k = 0
        while i**0.5 >= prem[k] and b:
            if i % prem[k] == 0:
                b = False
            k += 1
        if b:
            prem.append(i)
        i += 2
    return prem[-1]

# Finds whether n is prime
def IsPrime(n):
    if n % 2 == 0:
        return False
    i = 3
    while i <= n**0.5:
        if n % i == 0:
            return False
        i += 2
    return True

# Finds closest prime of n
def ClosestPrime(n):
    prem = [2,3,5]
    for i in range(7,n,2):
        b = True
        k = 0
        while i**0.5 >= prem[k] and b:
            if i % prem[k] == 0:
                b = False
            k += 1
        if b:
            prem.append(i)
    inf = prem[-1]
    sup = inf
    for i in range(n, n+ n-inf):
        b = True
        k = 0
        while i**0.5 >= prem[k] and b:
            if i % prem[k] == 0:
                b = False
            k += 1
        if b:
            sup = i
            break
    return max(inf,sup)

# Returns the decomposition of an integer
def DecompFactor(n):
    dec = []
    k = n
    i = 2
    while k != 1:
        if k % i == 0:
            dec.append(i)
            k /= i
        else:
            i += 1
    return dec
        
