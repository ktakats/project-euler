import math

def isPrime(num):
    if num==2:
        return True
    if num %2==0:
        return False
    for i in range(3, int(math.sqrt(num))+1,2):
        if num % i == 0:
            return False
    return True

def circulars(num):
    num=str(num)
    arr=list(num)
    for i in range(len(arr)-1):
        first=arr[0]
        arr.remove(first)
        arr.append(first)
        if not isPrime(int(''.join(arr))):
            return False
    return True

def allcirculars(N):
    circ=[0]*(N+1)
    for i in range(2,N+1):
        if isPrime(i):
            if circulars(i):
                circ[i]=i
    return circ



N=int(raw_input().strip())
circ=allcirculars(N)
print sum(circ)
