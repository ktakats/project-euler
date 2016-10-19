#Can't pass the last test

import math


def isPrime(num):
    if num==2:
        return True
    if num % 2==0:
        return False
    for i in range(3,int(math.sqrt(num)),2):
        if num%i ==0:
            return False
    return True

def nprime(lim):
    sieve = [True] * lim
    for i in range(3,int(math.sqrt(lim))+1,2):
        if sieve[i]:
            for j in range(i**2,lim,i):
                sieve[j]=False
    primes=[2]+[i for i in range(3,lim,2) if sieve[i]]
    return primes


N=int(raw_input().strip())

primes=nprime(N+1)
maxnumber=0
maxa=0
maxb=0
res=0
long(res)
for b in primes:
    for a in range(-N,N+1):
        lista=[]
        currnumber=0
        for n in range(100):
            res=n*n+a*n+b
            if res<=0 or not isPrime(res):
                break
            if not (res in lista):
                lista.append(res)

        if n>=maxnumber:
            maxnumber=n
            maxa=a
            maxb=b

print maxa, maxb
