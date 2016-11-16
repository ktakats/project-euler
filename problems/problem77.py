import math
def nprime():
    lim=1001
    sieve = [True] * lim
    for i in range(3,int(math.sqrt(lim))+1,2):
        if sieve[i]:
            for j in range(i**2,lim,i):
                sieve[j]=False
    primes=[2]+[i for i in range(3,lim,2) if sieve[i]]
    return primes

target = 2;
primes=nprime()

while True:
    ways = [0]*(target+1)
    ways[0] = 1;

    for i in range(len(primes)):
        #print primes[i]
        for j in range(primes[i], target+1):
            ways[j] += ways[j - primes[i]];


    if target == 1000:
        break
    target+=1

T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())
    print ways[N]
