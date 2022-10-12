# BigNumber, mpmath package required
# run this before execute: pip install BigNumber mpmath

import random

# https://www.delftstack.com/howto/python/python-generate-prime-number/
def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
            
    return prime_list

def make_keys(p, q):
    # place your own implementation of make_keys
    # use e = 65537 as if FIPS standard
    d=1
    e = 2
    n = p*q
    oiler = (p-1)*(q-1)
    def gcd(n1, n2):
        while n2 !=0:
            n1, n2 = n2, n1%n2
        return n1
    # e : public key
    while e< oiler and gcd(e, oiler)!=1:
        e+=1
    # d : primary key
    while(e*d) % oiler != 1 or d == e:
        d+=1


    return [e, d, n]

def rsa_encrypt(plain, e, n):
    # place your own implementation of rsa_encrypt
    return (plain**e)%n

def rsa_decrypt(cipher, d, n):
    # place your own implementation of rsa_decrypt
    return (cipher**d)%n

primes = primesInRange(100, 1000)

P = primes[random.randrange(0, len(primes))]
Q = primes[random.randrange(0, len(primes))]

while P == Q:
    P = primes[random.randrange(0, len(primes))]
    Q = primes[random.randrange(0, len(primes))]

M = random.randrange(2, 20)
e, d, N = make_keys(P, Q)
C = rsa_encrypt(M, e, N)
M2 = rsa_decrypt(C, d, N)

print(f"P = {P}, Q = {Q}, N = {N}, M = {M}, e = {e}, d = {d}, C = {C}, M2 = {M2}")

if M == M2:
    print("RSA Success!!")
else:
    print("RSA Failed...")
