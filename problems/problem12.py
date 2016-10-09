import math

def triangulars():
    lim=41042
    sumy=0
    div=0
    out={}
    for i in range(1,lim):
        sumy+=i
        j=num_divisors(sumy)
        if j>div:
            out[j]=sumy
            div=j
    return out

def nprime():
    lim=60000
    sieve = [True] * lim
    for i in range(3,int(math.sqrt(lim))+1,2):
        if sieve[i]:
            for j in range(i**2,lim,i):
                sieve[j]=False
    primes=[2]+[i for i in range(3,lim,2) if sieve[i]]
    return primes

def num_divisors(num):
    i=primes[0]
    k=0
    j=1
    count=0
    while(num>1):
        if num%i==0:
            count+=1
            num/=i
        else:
            j*=count+1
            k+=1
            i=primes[k]
            count=0
    j*=count+1
    return j


primes=nprime()
steps=triangulars()

T=int(raw_input().strip())

for t in range(T):
    N=int(raw_input().strip())
    out=[]
    for i in steps.keys():
        if i>N:
            out.append(i)
    print steps[min(out)]
