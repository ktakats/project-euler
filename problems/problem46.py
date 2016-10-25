import math

def nprime():
    lim=500000
    sieve = [True] * lim
    for i in range(3,int(math.sqrt(lim))+1,2):
        if sieve[i]:
            for j in range(i**2,lim,i):
                sieve[j]=False
    primes=[2]+[i for i in range(3,lim,2) if sieve[i]]
    return primes

primes=nprime() 

T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())
    count=0
    for num in primes:
        if num<N:
            if math.sqrt((N-num)/2.)==int(math.sqrt((N-num)/2.)):
                count+=1
        if num>=N:
            break
    print count
