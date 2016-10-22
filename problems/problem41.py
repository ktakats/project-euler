import math
import itertools

def isPrime(num):
    if num<2:
        return False
    if num==2:
        return True
    if num %2==0:
        return False
    for i in range(3, int(math.sqrt(num))+1,2):
        if num % i == 0:
            return False
    return True

def allpan():
    allpan=[]
#the test do not include numbers higher that 7 digits
    for digits in range(4,8):
        arr=range(1,digits+1)
        for perm in list(itertools.permutations(arr)):
            if perm[-1]%2!=0:
                num=int(''.join(str(i) for i in perm))
                if isPrime(num):
                      allpan.append(num)
    return allpan

allpan=allpan()

T=int(raw_input().strip())
for _ in range(T):
    N=int(raw_input().strip())
    if N<=1423:
        print -1
    else:
        arr=[i for i in allpan if i<=N]
        print arr[-1]
