import math

def sumOfDivisors(num):
    N=int(math.ceil(math.sqrt(num)))
    divs=1
    for i in range(2, N):
        if num % (i*1.)==0:
            divs+=i
            if num/i!=i:
                divs+=num/i

    return divs

def amicableNumbers():
    N=100000
    amicables=[0]*(N+1)
    for num in range(1, N+1):
        if amicables[num]==0:
            sumDivs=sumOfDivisors(num)
            if sumDivs>1 and sumDivs!=num:
                if sumOfDivisors(sumDivs)==num:
                    amicables[num]=num
                    if sumDivs<=N and sumDivs>num:
                        amicables[sumDivs]=sumDivs

    return amicables

def amicableSums():
    sums=[0]*100001
    sumsofar=0
    for i in range(1,100001):
        sumsofar+=amicables[i]
        sums[i]=sumsofar
    return sums

amicables=amicableNumbers()
sums=amicableSums()

T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())
    print sums[N]
