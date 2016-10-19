#Times out on Testcase 3
import math

def nprime():
    lim=10001
    sieve = [True] * lim
    for i in range(3,int(math.sqrt(lim))+1,2):
        if sieve[i]:
            for j in range(i**2,lim,i):
                sieve[j]=False
    primes=[2]+[i for i in range(3,lim,2) if sieve[i]]
    return primes

def longest(primes):
    longs=[]
    longestlength=1
    j=2
    for d in primes:
        m=1
        long(m)
        for n in range(1,d):
            m*=10
            if (m - 1) % d ==0:
                if n>longestlength:
                    longestlength=n
                    longs.append(d)
                break

    return longs

primes=nprime()
longs=longest(primes[:900])
T=int(raw_input().strip())
for _ in range(T):
    N=int(raw_input().strip())
    if N<=7:
        print 3
    elif N<=7000:
        arr=[i for i in longs if i<N]
        print arr[-1]
    else:
        arr=[i for i in primes[900:] if i>=N-50 and i<N]
        lon=longest(arr)
        print lon[-1]
