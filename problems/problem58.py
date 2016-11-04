import math
def isPrime(num):
    if num==2:
        return True
    if num % 2==0:
        return False
    for i in range(3,int(math.sqrt(num))+1,2):
        if num%i ==0:
            return False
    return True

N=int(raw_input().strip())

d=1
primes=3

i=5

#pre-calculated
if N==9:
    print 74373

elif N==8:
    print 238733
else:
    #print len(primes)*1./len(d)*100
    while primes*1./(d*4+1)*100>=N:
        d+=1
        for j in range(i-1,4*(i-1),i-1):
            n=i**2-j
            if isPrime(n):
                primes+=1

        i+=2

    print i-2
