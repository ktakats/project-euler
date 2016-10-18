import math

def goodie(num):
    arr=list(str(num))
    sumit=0
    for digit in arr:
        sumit+=math.factorial(int(digit))
    if (sumit*1.)%num==0 :
        return True
    return False

N=int(raw_input().strip())
goodlist=[0]
for num in range(10,N):
    if goodie(num):
        goodlist.append(num)
print sum(goodlist)
