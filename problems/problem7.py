import math

T=int(raw_input().strip())

def nprime():
    lim=110000
    sieve = [True] * lim
    for i in range(3,int(math.sqrt(lim))+1,2):
        if sieve[i]:
            for j in range(i**2,lim,i):
                sieve[j]=False
    primes=[2]+[i for i in range(3,lim,2) if sieve[i]]
    return primes


primes=nprime()
for t in range(T):
    N=int(raw_input().strip())
    print primes[N-1]
