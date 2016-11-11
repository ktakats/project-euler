import math


def nprime():
    lim=4000
    sieve = [True] * lim
    for i in range(3,int(math.sqrt(lim))+1,2):
        if sieve[i]:
            for j in range(i**2,lim,i):
                sieve[j]=False
    primes=[2]+[i for i in range(3,lim,2) if sieve[i]]
    return primes

def pandigital(num1,num):
    arr=list(str(num1))
    num=int(num)
    if len(list(str(num)))!=len(arr):
        return False
    for digit in list(str(num)):
        if digit in arr:
            arr.remove(digit)
        else:
            return False
    return True


N=int(raw_input().strip())
out=0
minsofar=1000000

primes=nprime()

for i,p in enumerate(primes):
    for j in range(i+1,len(primes)):
        for k in range(1,8):
            n=(p**k)*(primes[j])
            if n<N:
                prod=(n-n/p-n/primes[j]+n/(p*primes[j]))
                tot=(n*1.)/prod

                if pandigital(n,prod):
                    tot=round(tot,10)
                    if tot<minsofar:
                        minsofar=tot
                        out=n
                    elif tot==minsofar:
                        if n<out:
                            out=n
print out
