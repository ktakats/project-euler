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

def abundants():
    abundants=[]
    for i in range(12,28123):
        if sumOfDivisors(i)>i:
            abundants.append(i)
    return abundants

def checksum(N):
    for i in range(len(abundants)):
        if abundants[i] < N and N-abundants[i] in abundants:
            return True
    return False

def abundantSum(N):
    if N<24:
        return "NO"
    if N>28123:
        return "YES"
    else:
        if checksum(N):
            return "YES"
        else:
            return "NO"

abundants=abundants()
T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())
    print abundantSum(N)
