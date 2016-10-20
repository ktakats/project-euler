import math

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

def truncRight(num):
    num=str(num)
    for n in range(len(num)):
        num=num[1:]
        if num!='':
            if not isPrime(int(num)):
                return False
    return True

def truncLeft(num):
    num=str(num)
    for n in range(len(num)):
        num=num[:-1]
        if num!='':
            if not isPrime(int(num)):
                return False
    return True

N=int(raw_input().strip())
out=[]
for num in range(11,N,2):
    if isPrime(num):
        if truncRight(num):
            if truncLeft(num):
                out.append(num)

print sum(out)
