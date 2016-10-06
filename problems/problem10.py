import math

T=int(raw_input().strip())

def nprime():
    lim=1000001
    sieve = [True] * lim
    for i in range(3,int(math.sqrt(lim))+1,2):
        if sieve[i]:
            for j in range(i**2,lim,i):
                sieve[j]=False
    primes=[2]+[i for i in range(3,lim,2) if sieve[i]]
    return primes

def sumprimes(primes):
    out=[]
    sumy=0
    j=0
    for i in range(1000001):
        if primes[j]<=i:
            sumy+=primes[j]
            if j+1<len(primes):
                j+=1
        out.append(sumy)
    return out

primes=nprime()
sums=sumprimes(primes)
for t in range(T):
    N=int(raw_input().strip())
    print sums[N]
